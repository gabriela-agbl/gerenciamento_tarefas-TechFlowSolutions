# TaskFlow — Sistema de Gerenciamento de Tarefas

> Projeto desenvolvido para a disciplina de Engenharia de Software — UniFECAF
> Empresa fictícia: **TechFlow Solutions** | Cliente: startup de logística

---

## Objetivo

Desenvolver um sistema web de gerenciamento de tarefas baseado em metodologias ágeis, permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## Escopo Inicial

O sistema contempla as seguintes funcionalidades:

- **Criar** tarefas com título e descrição
- **Listar** tarefas organizadas por status em um quadro Kanban visual
- **Buscar** tarefas em tempo real pelo título ou descrição
- **Editar** título e descrição de uma tarefa existente
- **Atualizar status** movendo tarefas entre as colunas: A Fazer → Em Progresso → Concluído
- **Deletar** tarefas
- Persistência local em arquivo JSON

---

## Mudança de Escopo

**Data:** 30/05/2026
**Justificativa:** Durante o desenvolvimento, identificou-se que a startup de logística necessita diferenciar tarefas urgentes das demais para priorização operacional. Por isso, foi adicionado o campo `prioridade` com os valores `baixa`, `media` e `alta`, ampliando o escopo inicial que previa apenas título e descrição.
**Impacto:** Novo card criado no Kanban, função `criar_tarefa` atualizada para aceitar o parâmetro de prioridade, interface web atualizada para exibir e filtrar por prioridade.

---

## Metodologia Ágil

O projeto adota **Kanban** como metodologia principal, com o quadro organizado em três colunas:

| Coluna | Descrição |
|--------|-----------|
| A Fazer | Tarefas planejadas ainda não iniciadas |
| Em Progresso | Tarefas em desenvolvimento ativo |
| Concluído | Tarefas concluídas e validadas |

As iterações seguem ciclos curtos com revisão contínua das prioridades, alinhado aos princípios do Manifesto Ágil.

---

## Estrutura do Repositório

```
taskflow/
├── src/
│   ├── main.py               # Aplicação Flask — rotas e operações CRUD
│   ├── main_data.json       # Arquivo de persistência (gerado automaticamente)
│   └── templates/
│       └── index.html        # Interface web — quadro Kanban
├── tests/
│   └── test_main.py          # Testes unitários com Pytest
├── docs/                     # Documentação adicional e diagramas UML
├── .github/
│   └── workflows/
│       └── ci.yml            # Pipeline de integração contínua
├── requirements.txt          # Dependências do projeto
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
git clone https://github.com/gabriela-agbl/gerenciamento_tarefas-TechFlowSolutions.git
cd taskflow
pip install -r requirements.txt
```

### Rodando a aplicação

```bash
python src/main.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

### Rodando os testes

```bash
pytest tests/ -v
```

### Verificando cobertura de testes

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Funcionalidades da Interface

| Funcionalidade | Descrição |
|----------------|-----------|
| Criar tarefa | Formulário no topo da página com título e descrição |
| Visualizar Kanban | Tarefas organizadas automaticamente nas 3 colunas |
| Buscar | Barra de busca em tempo real por título ou descrição |
| Editar | Botão ✏ em cada card abre formulário inline |
| Mover status | Botões → Em Progresso, ✓ Concluir, ← Voltar, ← Reabrir |
| Deletar | Botão ✕ em cada card remove a tarefa |

---

## Integração Contínua (CI)

O projeto utiliza **GitHub Actions** para executar automaticamente os testes a cada `push` ou `pull request` na branch `main`. O pipeline:

1. Configura o ambiente Python 3.12
2. Instala as dependências via `requirements.txt`
3. Executa todos os testes unitários com Pytest
4. Exibe o relatório de cobertura de código

---

## Testes Automatizados

Os testes cobrem todas as operações CRUD:

| Operação | Testes |
|----------|--------|
| Criar | Título válido, com descrição, título vazio, IDs incrementais |
| Listar | Lista vazia, todas as tarefas, filtro por status |
| Buscar | ID existente, ID inexistente |
| Atualizar | Status, título, status inválido, ID inexistente |
| Deletar | Tarefa existente, ID inexistente |

Execute com cobertura:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.12 | Linguagem principal |
| Flask 3.0 | Framework web |
| Pytest | Testes unitários |
| pytest-cov | Cobertura de testes |
| GitHub Actions | Integração contínua |
| GitHub Projects | Gestão ágil (Kanban) |
| JSON | Persistência de dados |