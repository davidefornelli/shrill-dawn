# Tutorial https://dev.to/yankee/streamline-projects-using-makefile-28fe
.DEFAULT_GOAL := it

VENV ?= .venv
REQUIREMENTS_FILE ?= requirements.txt

it: # Configure python enironment
	@echo "Create venv"
	@python3 -m venv $(VENV)
	@echo "Update pip"
	@$(VENV)/bin/python -m pip -q install --upgrade pip
	@echo "Installing requirements"
	@$(VENV)/bin/python -m pip -q install -r $(REQUIREMENTS_FILE)
	@echo "Create git repository"
	@$(VENV)/bin/python main.py
