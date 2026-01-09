PY=python3
VENV=.venv
BIN=$(VENV)/bin

.PHONY: venv install kernel notebook clean

venv:
	$(PY) -m venv $(VENV)

install: venv
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

kernel: install
	$(BIN)/python -m ipykernel install --user --name talent-retention --display-name "Python (talent-retention)"

notebook: install
	$(BIN)/jupyter notebook

clean:
	rm -rf $(VENV)
