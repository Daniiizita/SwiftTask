# SwiftTask

## Descrição do Projeto

SwiftTask é uma aplicação web desenvolvida em Django para controle de tarefas e registro de tempo de trabalho. O sistema permite o cadastro de tarefas, registro de tempos associados a essas tarefas e oferece funcionalidades de listagem com filtros sobre o tempo de trabalho cadastrado por cada usuário.

## Funcionalidades

1. **Cadastro de Tarefas**
    - Nome do usuário responsável
    - Data de criação
    - Descrição

2. **Registro de Tempo de Trabalho**
    - Data do registro
    - Quantidade de horas ou minutos trabalhados
    - Descrição do trabalho realizado
    - Relacionamento com uma tarefa

3. **Listagem**
    - Página para listar todas as tarefas
    - Página para listar todos os registros de tempo
    - Funcionalidades de filtragem nos registros de tempo por data, quantidade de horas, descrição, usuário, tarefa, etc.

## Requisitos Técnicos

- Python
- Django
- Git

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

### Passo a Passo

1. **Clone o repositório:**

    ```bash
    git clone <https://github.com/Daniiizita/SwiftTask>
    cd SwiftTask
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

6. **Acesse a aplicação:**
    Abra o navegador e vá para `http://127.0.0.1:8000/`

## Contato

Para dúvidas ou mais informações, entre em contato pelo e-mail: [goncalvesdani54@tianalista.onmicrosoft.com](mailto:goncalvesdani54@tianalista.onmicrosoft.com)
