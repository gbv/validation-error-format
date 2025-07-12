default: .venv
.venv:
	python -mvenv .venv
	.venv/bin/pip install -r requirements.txt

dev: .venv
	.venv/bin/pip install ruff
		
lint:
	. .venv/bin/activate && ruff format xml-validate validation_error/* xml_validator/*

.PHONY: test
test:
	pytest
	./test.sh
