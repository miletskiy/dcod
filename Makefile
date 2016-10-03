# -*- makefile -*-
SHELL=/bin/bash
# Copyright (с) 2016.

# constants
PROJECT_NAME=DCOD
BIND_TO=0.0.0.0
BIND_PORT=8022
MANAGE=python manage.py
DJANGO_SETTINGS_MODULE=dcod.settings

TEST_APP=apps
TEST_OPTIONS=-v2 --keepdb

include

.PHONY: run open local clean manage help test flake8 shell ishell hshell push github

run:
	@echo Starting $(PROJECT_NAME) with $(DJANGO_SETTINGS_MODULE)...
	$(MANAGE) runserver $(BIND_TO):$(BIND_PORT) --settings=$(DJANGO_SETTINGS_MODULE)

open:
	@echo Opening $(PROJECT_NAME) ...
	open 'http://$(BIND_TO):$(BIND_PORT)'

local:
	@echo Starting local $(PROJECT_NAME) ...
	heroku local web

web:
	@echo Opening web version $(PROJECT_NAME) ...
	heroku open

clean:
	@echo Cleaning up...
	find ./dcod | grep '\.pyc$$' | xargs -I {} rm {}
	find ./apps/core | grep '\.pyc$$' | xargs -I {} rm {}
	# find ./dcod | grep '\.pyc$$' | xargs -p -I {} rm {}
	@echo Done

manage:
ifndef cmd
	@echo Please, specify cmd=command argument to execute
else
	$(MANAGE) $(cmd) --settings=$(DJANGO_SETTINGS_MODULE)
endif

test:
	$(MANAGE) test $(TEST_APP) $(TEST_OPTIONS)

flake8:
	@echo Please, configure this command
	@echo http://flake8.pycqa.org/en/latest/config.html
	flake8 --max-complexity 10 $(TEST_APP)

shell:
	# @echo Please, specify this command in the Makefile
	$(MANAGE) shell --plain

hshell:
	@echo Connecting to the Heroku django-shell
	heroku run $(MANAGE) shell

ishell:
	$(MANAGE) shell -i ipython

push:
	git push heroku master

github:
	git push



# SHELL := /bin/sh
LOCALPATH := ./src
PYTHONPATH := $(LOCALPATH)/
# PROJECT := someproject
PYTHON_BIN := $(VIRTUAL_ENV)/bin

showenv:
	@echo 'Environment:'
	@echo '-----------------------'
	@$(PYTHON_BIN)/python -c "import sys; print 'sys.path:', sys.path"
	@echo 'PYTHONPATH:' $(PYTHONPATH)
	@echo 'PROJECT:' $(PROJECT_NAME)
	@echo 'DJANGO_SETTINGS_MODULE:' $(DJANGO_SETTINGS_MODULE)
	@echo 'DJANGO_LOCAL_SETTINGS_MODULE:' $(DJANGO_LOCAL_SETTINGS_MODULE)
	@echo 'DJANGO_TEST_SETTINGS_MODULE:' $(DJANGO_TEST_SETTINGS_MODULE)

help:
	@cat README.md

# https://github.com/kaleissin/django-makefile/blob/master/Makefile
