# 🧪 Automação de Testes Web com Selenium + Python

Este projeto contém a automação de testes end-to-end (E2E) para a aplicação **SauceDemo**, utilizando **Python, Selenium WebDriver e Pytest**, seguindo o padrão **Page Object Model (POM)**.

---

## 🎯 Objetivo

Validar os principais fluxos da aplicação, garantindo a qualidade e o correto funcionamento das funcionalidades críticas, como:

* Login
* Adição e remoção de produtos
* Carrinho de compras
* Checkout
* Ordenação de produtos

---

## 🛠️ Tecnologias utilizadas

* Python 🐍
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

---

## 📂 Estrutura do projeto

```
selenium-web-automation-tests
│
├── pages/                 # Page Objects (camadas de interação com a UI)
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                 # Casos de teste
│   ├── test_CT01_valid_login.py
│   ├── test_CT02_login_error.py
│   ├── test_CT03_locked_used_login.py
│   ├── test_CT04_cart_add_products.py
│   ├── test_CT05_add_all_products_to_cart.py
│   ├── test_CT06_checkout_sucess.py
│   ├── test_CT07_checkout_missing_fields.py
│   ├── test_CT08_remove_product_from_cart.py
│   └── test_CT09_sort_products_by_price.py
│
├── reports/               # Relatórios e screenshots
├── conftest.py            # Configuração de fixtures
├── requirements.txt       # Dependências
└── README.md
```

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <https://github.com/nathbellis/test-automation-framework-selenium>
cd test-automation-framework-selenium
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar os testes

```bash
pytest
```

---

## 🧪 Tipos de testes implementados

### 🔐 Login

* Login com credenciais válidas
* Login com credenciais inválidas
* Usuário bloqueado

### 🛒 Carrinho

* Adicionar produtos
* Remover produtos
* Validar quantidade de itens
* Adicionar múltiplos produtos

### 💳 Checkout

* Finalizar compra com sucesso
* Validação de campos obrigatórios

### 🔄 Ordenação

* Ordenação por preço (crescente e decrescente)

---

## 🏷️ Uso de markers (Pytest)

Os testes estão organizados com markers:

```bash
pytest -m smoke
pytest -m login
pytest -m cart
pytest -m checkout
pytest -m sort
```

---

## 📸 Evidências

Em caso de falha, screenshots são automaticamente capturadas e salvas em:

```
reports/screenshots/
```

---

## 💡 Boas práticas aplicadas

* Page Object Model (POM)
* Separação entre ações e validações
* Uso de parametrização com Pytest
* Estrutura organizada e escalável
* Uso de waits explícitos para estabilidade
* Testes independentes e reutilizáveis

---

## 🧠 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos importantes de QA, como:

* Criação de testes robustos e confiáveis
* Redução de flakiness
* Validação de regras de negócio
* Organização de framework de automação

---

## 👩‍💻 Autora

Projeto desenvolvido por **Nathalia De Bellis Gomes Anselmo**, com foco em desenvolvimento na área de Qualidade de Software (QA) e automação de testes.

---

