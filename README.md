
# POSCOMP-Unilab

**POSCOMP-Unilab** é uma interface desenvolvida para apoiar estudantes da área de Computação que desejam ingressar na pós-graduação.
O projeto tem como objetivo **facilitar o acesso às provas antigas do POSCOMP** de forma gratuita, organizada e acessível.

---

## Objetivo

* Centralizar provas anteriores do POSCOMP em uma única interface.
* Oferecer uma forma prática e gratuita para que os estudantes possam estudar.
* Apoiar o processo de preparação para programas de mestrado e doutorado em Computação.

---

## Tecnologias utilizadas

* **Flask (Python)** – Backend da aplicação.
* **HTML + CSS + JavaScript** – Estrutura e estilo da interface.
---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/poscomp-unilab.git
cd poscomp-unilab
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
flask run
```


## Estrutura do projeto

```
poscomp-unilab/
│── static/          # Arquivos CSS, JS, imagens
│── templates/       # Páginas HTML
│── app.py   # Arquivo principal Flask
│── requirements.txt # Dependências do projeto
│── README.md        # Este arquivo
```

---

##  Funcionalidades (previstas/implementadas)

* [x] Interface simples e responsiva.
* [x] Acesso a provas anteriores do POSCOMP.
* [x] Filtros de busca por ano.
* [x] Filtros de busca por assunto.
* [ ] Área de login para salvar provas favoritas.
* [ ] Estatísticas de questões por tema.

---

## Contribuição

Contribuições são bem-vindas!
Para contribuir:

1. Faça um **fork** do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Commit suas alterações: `git commit -m 'Adiciona minha feature'`.
4. Faça o push: `git push origin minha-feature`.
5. Abra um **Pull Request**.

---

## Licença

Este projeto é de uso **educacional e gratuito**.

---

## Autores

1. Ivina Lorena Oliveira Moura

