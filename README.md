# TaskFlow — Sistema de Gerenciamento de Tarefas

> Projeto desenvolvido para a disciplina de Engenharia de Software — UniFECAF  
> Empresa fictícia: **TechFlow Solutions** | Cliente: startup de logística

---

## Objetivo

Desenvolver um sistema de gerenciamento de tarefas baseado em metodologias ágeis, permitindo acompanhar o fluxo de trabalho, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## Escopo Inicial

O sistema contempla as seguintes funcionalidades:

- **Criar** tarefas com título, descrição e prioridade
- **Listar** tarefas com filtro por status
- **Buscar** tarefa por ID
- **Atualizar** campos de uma tarefa (título, descrição, prioridade, status)
- **Deletar** tarefa por ID
- Persistência local em arquivo JSON

---

## Estrutura do Repositório

```
taskflow/
├── src/
│   └── main.py          # Módulo principal — operações CRUD
├── tests/
│   └── test_main.py     # Testes unitários com Pytest
├── docs/                 # Documentação adicional e diagramas UML
├── .github/
│   └── workflows/
│       └── ci.yml        # Pipeline de integração contínua
├── .gitignore
├── LICENSE
└── README.md
```

---

## Como Executar

### Pré-requisitos

- Python 3.9 ou superior
- pip

### Instalação

```bash
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow
pip install pytest pytest-cov
```

### Rodando os testes

```bash
pytest tests/ -v
```

### Exemplo de uso no código

```python
from src.tasks import criar_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa

# Criar uma tarefa
tarefa = criar_tarefa("Implementar autenticação", prioridade="alta")

# Listar todas as tarefas
todas = listar_tarefas()

# Mover para em progresso
atualizar_tarefa(tarefa["id"], status="em_progresso")

# Concluir e deletar
atualizar_tarefa(tarefa["id"], status="concluido")
deletar_tarefa(tarefa["id"])
```

---

## Integração Contínua (CI)

O projeto utiliza **GitHub Actions** para executar automaticamente os testes a cada `push` ou `pull request` na branch `main`. O pipeline:

1. Configura o ambiente Python 3.11
2. Instala as dependências (pytest, pytest-cov)
3. Executa todos os testes unitários
4. Exibe o relatório de cobertura de código

---

## Testes Automatizados

Os testes cobrem todos os casos das operações CRUD:

- Criação com dados válidos e inválidos
- Listagem completa e filtrada por status
- Busca por ID existente e inexistente
- Atualização de campos e validação de valores
- Deleção e tentativa de deleção de IDs inexistentes

Execute com cobertura:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.11 | Linguagem principal |
| Pytest | Testes unitários |
| pytest-cov | Cobertura de testes |
| GitHub Actions | Integração contínua |
| GitHub Projects | Gestão ágil (Kanban) |