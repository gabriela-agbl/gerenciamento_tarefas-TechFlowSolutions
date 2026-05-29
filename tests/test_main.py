import os
import pytest
import tempfile

import sys
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
    tarefa = criar_tarefa("Tarefa com descricao", descricao="Detalhes aqui", caminho=arquivo_temp)
    assert tarefa["descricao"] == "Detalhes aqui"

def test_criar_tarefa_titulo_vazio_levanta_erro(arquivo_temp):
    with pytest.raises(ValueError, match="título"):
        criar_tarefa("", caminho=arquivo_temp)