from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "techflow_secret_key"

TASKS_FILE = os.path.join(os.path.dirname(__file__), "main_data.json")

def _carregar_tarefas(caminho: str = TASKS_FILE) -> list:
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return []
        return json.loads(conteudo)


def _salvar_tarefas(tarefas: list, caminho: str = TASKS_FILE) -> None:
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def criar_tarefa(titulo: str, descricao: str = "", caminho: str = TASKS_FILE) -> dict:
    if not titulo or not titulo.strip():
        raise ValueError("O título da tarefa não pode ser vazio.")

    tarefas = _carregar_tarefas(caminho)
    novo_id = max((t["id"] for t in tarefas), default=0) + 1

    tarefa = {
        "id": novo_id,
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "status": "a_fazer",
        "criado_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "atualizado_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    tarefas.append(tarefa)
    _salvar_tarefas(tarefas, caminho)
    return tarefa


def listar_tarefas(status: str = None, caminho: str = TASKS_FILE) -> list:
    tarefas = _carregar_tarefas(caminho)
    if status:
        tarefas = [t for t in tarefas if t["status"] == status]
    return tarefas


def buscar_tarefa(tarefa_id: int, caminho: str = TASKS_FILE) -> dict:
    tarefas = _carregar_tarefas(caminho)
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa
    raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")


def atualizar_tarefa(tarefa_id: int, caminho: str = TASKS_FILE, **campos) -> dict:
    campos_validos = {"titulo", "descricao", "status"}
    status_validos = {"a_fazer", "em_progresso", "concluido"}

    for campo in campos:
        if campo not in campos_validos:
            raise ValueError(f"Campo inválido: '{campo}'.")

    if "status" in campos and campos["status"] not in status_validos:
        raise ValueError(f"Status inválido. Use: {status_validos}")

    if "titulo" in campos and not campos["titulo"].strip():
        raise ValueError("O título não pode ser vazio.")

    tarefas = _carregar_tarefas(caminho)
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa.update(campos)
            tarefa["atualizado_em"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            _salvar_tarefas(tarefas, caminho)
            return tarefa

    raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")


def deletar_tarefa(tarefa_id: int, caminho: str = TASKS_FILE) -> bool:
    tarefas = _carregar_tarefas(caminho)
    tarefas_filtradas = [t for t in tarefas if t["id"] != tarefa_id]

    if len(tarefas_filtradas) == len(tarefas):
        raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")

    _salvar_tarefas(tarefas_filtradas, caminho)
    return True

@app.route("/")
def index():
    tarefas = _carregar_tarefas()
    a_fazer = [t for t in tarefas if t["status"] == "a_fazer"]
    em_progresso = [t for t in tarefas if t["status"] == "em_progresso"]
    concluido = [t for t in tarefas if t["status"] == "concluido"]
    return render_template("index.html",
                           a_fazer=a_fazer,
                           em_progresso=em_progresso,
                           concluido=concluido)


@app.route("/criar", methods=["POST"])
def criar():
    titulo = request.form.get("titulo", "")
    descricao = request.form.get("descricao", "")
    try:
        criar_tarefa(titulo, descricao)
        flash("Tarefa criada com sucesso!", "sucesso")
    except ValueError as e:
        flash(str(e), "erro")
    return redirect(url_for("index"))


@app.route("/atualizar/<int:tarefa_id>", methods=["POST"])
def atualizar(tarefa_id):
    novo_status = request.form.get("status")
    try:
        atualizar_tarefa(tarefa_id, status=novo_status)
        flash("Tarefa atualizada!", "sucesso")
    except ValueError as e:
        flash(str(e), "erro")
    return redirect(url_for("index"))


@app.route("/deletar/<int:tarefa_id>", methods=["POST"])
def deletar(tarefa_id):
    try:
        deletar_tarefa(tarefa_id)
        flash("Tarefa removida!", "sucesso")
    except ValueError as e:
        flash(str(e), "erro")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)