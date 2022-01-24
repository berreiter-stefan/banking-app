SHELL := /bin/bash
.ONESHELL:
.PHONY: test

DIR_CODE = "banking_app"
DIR_VENV = "venv"

venv-new:
	# removes the virtual environment if existing,
	# creates a new virtual env, activates it and installs the requirements
	cd ${DIR_CODE};
	if [ -d ${DIR_VENV} ]; then rm -r ${DIR_VENV}; fi
	python3 -m ${DIR_VENV} ./${DIR_VENV}; \
	source ${DIR_VENV}/bin/activate; \
	pip install -r requirements.txt

venv-clean:
	rm -r ${DIR_VENV}; # cleans virtual environment

postgres-up:
	docker-compose up -d

postgres-down:
	docker-compose down

build:
	python3 ${DIR_CODE}/main.py

test:
	PYTHONPATH=. pytest

polish:
	black .
	pylint banking_app/
