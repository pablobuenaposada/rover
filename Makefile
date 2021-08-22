venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv .pytest_cache

format/isort: venv
	venv/bin/isort src

format/black: venv
	venv/bin/black --verbose src

format: venv format/isort format/black

test: venv
	PYTHONPATH=src venv/bin/pytest src/tests

run: venv
	PYTHONPATH=src venv/bin/python src/main.py --output=$(output) --input=$(input)

docker/build:
	docker build --no-cache	--tag=rover .

docker/run:
	 docker run --rm -it -v $(shell pwd)/output/:/usr/src/app/output/ rover

docker/test:
	 docker run rover /bin/sh -c 'make test'
