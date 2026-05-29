import json
import os
from datetime import datetime

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
        raise ValueError("Por favor, coloque um nome na tarefa!")
    
    tarefas = _carregar_tarefas(caminho)

    novo_id = max((t["id"] for t in tarefas), default=0) + 1

    tarefa = {
        "id": novo_id,
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "status": "a_fazer",
        "criado_em": datetime.now().isoformat(),
        "atualizado_em": datetime.now().isoformat(),
    }

    tarefas.append(tarefa)
    _salvar_tarefas(tarefas, caminho)
    
    return tarefa

def listar_tarefas(status: str = None, caminho: str = TASKS_FILE) -> list:
    tarefas = _carregar_tarefas(caminho)
    if status:
        tarefas = [t for t in tarefas if t["status"] == status]
    return tarefas