venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv .pytest_cache sitters.csv

format/isort: venv
	venv/bin/isort src

format/black: venv
	venv/bin/black --verbose src

format: venv format/isort format/black

test: venv
	PYTHONPATH=src venv/bin/pytest src/tests

run: venv
	PYTHONPATH=src venv/bin/python src/main.py