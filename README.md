# 🎬 HashFlix

**HashFlix** é uma plataforma de cursos online desenvolvida com **Python e Django**, inspirada na Netflix. A aplicação permite adicionar cursos, aulas e vídeos, oferecendo ao usuário uma experiência de navegação semelhante à  plataforma do streaming.

---

## 🌐 Demonstração

A aplicação está disponível online:

https://hashflix-production-2895.up.railway.app/filmes/

---

## 📚 Sobre o projeto

O **HashFlix** foi desenvolvido como um projeto prático para estudar desenvolvimento web com Django, aplicando conceitos de criação de aplicações completas, organização de conteúdo e deploy em produção.

A plataforma permite cadastrar cursos e aulas, que podem ser gerenciados facilmente através do Django Admin.

---

## ⚙️ Tecnologias utilizadas

* Python
* Django
* HTML
* CSS
* TailwindCSS
* PostgreSQL
* Gunicorn
* Whitenoise
* Railway (deploy)

---

## ✨ Funcionalidades

✔️ Sistema de autenticação de usuários  
✔️ Edição de perfil  
✔️ Alteração de senha  
✔️ Catálogo de cursos  
✔️ Pesquisa de cursos  
✔️ Aulas  
✔️ Sistema de comentários  
✔️ Gerenciamento de conteúdos pelo Django Admin  
✔️ Interface inspirada em plataforma da Netflix.

---

## 🚀 Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/hashflix.git
cd hashflix
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migrações

```bash
python manage.py migrate
```

### 5️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

### 6️⃣ Rodar servidor

```bash
python manage.py runserver
```

Acesse no navegador:

http://127.0.0.1:8000

Admin:

http://127.0.0.1:8000/admin

---

⚠️ Configuração de DEBUG para desenvolvimento

No arquivo settings.py, o projeto vem configurado com o modo de depuração desativado:

DEBUG = False

Para executar o projeto em ambiente de desenvolvimento local, altere para:

DEBUG = True

Isso permitirá visualizar erros detalhados no navegador e facilitar o desenvolvimento da aplicação.

## 📂 Estrutura do projeto

```
hashflix/
│
├── filmes/
├── contas/
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para:

* Praticar desenvolvimento web com Django
* Criar uma plataforma funcional de cursos online
* Aprender a estruturar aplicações completas em Python
* Trabalhar com deploy de aplicações em produção

---

## 🔮 Possíveis melhorias futuras


* Controle de progresso das aulas
* Sistema de pagamentos

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo e prática de desenvolvimento web com **Python e Django**.
