format/isort:
	@venv/bin/isort src

format/black:
	@venv/bin/black --verbose src

format: format/isort format/black

test:
	@venv/bin/pytest src/tests
