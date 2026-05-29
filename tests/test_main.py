import os
import pytest
import tempfile

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import criar_tarefa, listar_tarefas, buscar_tarefa, atualizar_tarefa, deletar_tarefa