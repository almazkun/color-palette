REGISTRY = ghcr.io/almazkun
APP_NAME = color-palette
CONTAINER_NAME = color-palette-container
EXECUTOR = pipenv
COMMAND = run
k = .

.PHONY: help

help:
	cat Makefile

lint:
	$(EXECUTOR) $(COMMAND) ruff check --fix -e .
	$(EXECUTOR) $(COMMAND) black .

cov:
	$(EXECUTOR) $(COMMAND) pip install coverage
	$(EXECUTOR) $(COMMAND) coverage run ./manage.py test ./tests
	$(EXECUTOR) $(COMMAND) coverage html
	$(EXECUTOR) $(COMMAND) coverage report -m

test:
	$(EXECUTOR) $(COMMAND) ./manage.py test ./tests -k=$(k)

run:
	$(EXECUTOR) $(COMMAND) ./manage.py runserver

migrate:
	$(EXECUTOR) $(COMMAND) ./manage.py migrate

makemigrations:
	$(EXECUTOR) $(COMMAND) ./manage.py makemigrations

makemessages:
	$(EXECUTOR) $(COMMAND) ./manage.py makemessages -a

collectstatic:
	$(EXECUTOR) $(COMMAND) ./manage.py collectstatic

startdemo:
	$(EXECUTOR) $(COMMAND) ./manage.py startdemo

shell:
	$(EXECUTOR) $(COMMAND) ./manage.py shell

build:
	docker build -t $(REGISTRY)/$(APP_NAME) .

prod:
	docker run -it -p 8000:8000 --rm -d --name $(CONTAINER_NAME) --env-file ./.env $(REGISTRY)/$(APP_NAME)