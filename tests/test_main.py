import os
import sys
import pytest
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import criar_tarefa, listar_tarefas, buscar_tarefa, atualizar_tarefa, deletar_tarefa

@pytest.fixture
def arquivo_temp():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        caminho = f.name
    yield caminho
    os.unlink(caminho)

def test_criar_tarefa_basica(arquivo_temp):
    tarefa = criar_tarefa("Implementar login", caminho=arquivo_temp)
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Implementar login"
    assert tarefa["status"] == "a_fazer"

def test_criar_tarefa_com_descricao(arquivo_temp):
    tarefa = criar_tarefa("Tarefa", descricao="Detalhes aqui", caminho=arquivo_temp)
    assert tarefa["descricao"] == "Detalhes aqui"

def test_criar_tarefa_titulo_vazio_levanta_erro(arquivo_temp):
    with pytest.raises(ValueError, match="não pode ser vazio"):
        criar_tarefa("", caminho=arquivo_temp)

def test_ids_incrementais(arquivo_temp):
    t1 = criar_tarefa("T1", caminho=arquivo_temp)
    t2 = criar_tarefa("T2", caminho=arquivo_temp)
    t3 = criar_tarefa("T3", caminho=arquivo_temp)
    assert t1["id"] == 1
    assert t2["id"] == 2
    assert t3["id"] == 3

def test_listar_tarefas_vazio(arquivo_temp):
    assert listar_tarefas(caminho=arquivo_temp) == []

def test_listar_tarefas_retorna_todas(arquivo_temp):
    criar_tarefa("T1", caminho=arquivo_temp)
    criar_tarefa("T2", caminho=arquivo_temp)
    assert len(listar_tarefas(caminho=arquivo_temp)) == 2

def test_listar_tarefas_com_filtro_status(arquivo_temp):
    criar_tarefa("T1", caminho=arquivo_temp)
    t2 = criar_tarefa("T2", caminho=arquivo_temp)
    atualizar_tarefa(t2["id"], status="em_progresso", caminho=arquivo_temp)
    em_progresso = listar_tarefas(status="em_progresso", caminho=arquivo_temp)
    assert len(em_progresso) == 1
    assert em_progresso[0]["titulo"] == "T2"

def test_buscar_tarefa_existente(arquivo_temp):
    criada = criar_tarefa("Buscar isso", caminho=arquivo_temp)
    encontrada = buscar_tarefa(criada["id"], caminho=arquivo_temp)
    assert encontrada["titulo"] == "Buscar isso"

def test_buscar_tarefa_inexistente_levanta_erro(arquivo_temp):
    with pytest.raises(ValueError, match="não encontrada"):
        buscar_tarefa(999, caminho=arquivo_temp)

def test_atualizar_status(arquivo_temp):
    tarefa = criar_tarefa("T", caminho=arquivo_temp)
    atualizada = atualizar_tarefa(tarefa["id"], status="em_progresso", caminho=arquivo_temp)
    assert atualizada["status"] == "em_progresso"

def test_atualizar_titulo(arquivo_temp):
    tarefa = criar_tarefa("Título antigo", caminho=arquivo_temp)
    atualizada = atualizar_tarefa(tarefa["id"], titulo="Título novo", caminho=arquivo_temp)
    assert atualizada["titulo"] == "Título novo"

def test_atualizar_status_invalido_levanta_erro(arquivo_temp):
    tarefa = criar_tarefa("T", caminho=arquivo_temp)
    with pytest.raises(ValueError, match="Status inválido"):
        atualizar_tarefa(tarefa["id"], status="pausado", caminho=arquivo_temp)

def test_atualizar_tarefa_inexistente_levanta_erro(arquivo_temp):
    with pytest.raises(ValueError, match="não encontrada"):
        atualizar_tarefa(999, status="concluido", caminho=arquivo_temp)

def test_deletar_tarefa(arquivo_temp):
    tarefa = criar_tarefa("Remover", caminho=arquivo_temp)
    assert deletar_tarefa(tarefa["id"], caminho=arquivo_temp) is True
    assert listar_tarefas(caminho=arquivo_temp) == []

def test_deletar_tarefa_inexistente_levanta_erro(arquivo_temp):
    with pytest.raises(ValueError, match="não encontrada"):
        deletar_tarefa(999, caminho=arquivo_temp)