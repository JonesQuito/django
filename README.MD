## DJANGO COM POSTGRES

############################# DJANGO COM POSTGRES ##################################
1 - CRIAR UM VIRTUALENV
2 - INSTALAR psycopg2 COM O COMANDO 	'pip install psycopg2 django'
3 - EXECUTAR O COMANDO pip freeze PARA VISUALIZAR AS DEPENDENCIAS DO VENV
4 - CRIAR O ARQUIVO 'requiriments.txt' NA VENV
5 - CRIAR UM PROJETO 'django-admin.py startproject nome_projeto'
6 - ACESSAR A PASTA DO PROJETO
7 - CRIAR UM APP 'python manage.py startapp nome_app'
8 - MOVER A PASTA DO APP PARA DENTRO DO PROJETO
9 - MOVER O models.py PARA A RAÍZ PROJETO (myproject/myproject)
10- ADICIONAR O PROJETO E O APP NA LISTA DE APPS INSTALADOS NO 	settings.py
			Ex: 'nome_projeto', nome_projeto.nome_app

11- NO settings.py EDITAR O DICIONARIO DE CONEXÃO COM O BANCO:
			DATABASES = {
    			'default': {
        		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		        'NAME': 'mydb',
		        # 'NAME': os.path.join(BASE_DIR, 'mydb'),
		        'USER': 'myuser',
		        'PASSWORD': 'mypassword',
		        'HOST': '127.0.0.1',
		        'PORT': '', # 8000 is default
			    }
			}

12- CONFIGURAR AS ursl DO PROJETO E DO APP
13- EXECUTAR O 'python manage.py makemigratiosn'
14- EXECUTAR O 'python manage.py migrate'
15- INICIAR O SERVIDOR DE APLICAÇÃO 'python manage.py runserver'

OS COMANDOS DOS PASSOS 13 E 14 SÃO RESPONSÁVEIS POR CRIAR AS TABELAS NO BANCO DE DADOS

LIKS ÚTEI: http://pythonclub.com.br/postgresql-e-django.html