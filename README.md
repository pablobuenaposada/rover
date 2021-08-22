# Generated CSV file
You will find a copy of the generated csv in `output/sitters.csv`.

# Usage with Docker
Step in project folder: 
```bash
cd Rover-Takehome-Web/
```
Build docker image with:
```bash
make docker/build
```

### Run CSV generator
do:
```bash
make docker/run
```
would output something like:
```bash
docker run --rm -it -v /Users/pablobuenaposada/Desktop/rover/output/:/usr/src/app/output/ rover
PYTHONPATH=src venv/bin/python src/main.py --output=output/sitters_docker.csv --input=
Reading: reviews.csv
Writing: output/sitters_docker.csv
```
then check inside `output/` folder you should have a file called `sitters_docker.csv` that has been extracted from the docker container to your local.
```bash
pablobuenaposada$ cat output/sitters_docker.csv
email,name,profile_score,ratings_score,search_score
user7508@t-mobile.com,Leilani R.,1.15,3.5,3.5
user9029@t-mobile.com,Melissa C.,1.35,4.0,2.94
user7903@hotmail.com,Faridah D.,1.15,4.6,2.88
user7650@verizon.net,Robert S.,1.15,3.57,2.85
...
```

### Run tests
```bash
make docker/test
```
output:
```bash
docker run rover /bin/sh -c 'make test'
PYTHONPATH=src venv/bin/pytest src/tests
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /usr/src/app
collected 44 items

src/tests/test_main.py .                                                 [  2%]
src/tests/csv_utils/test_csv_utils.py .......                            [ 18%]
src/tests/models/test_sitter.py ................................         [ 90%]
src/tests/models/test_sitters.py ....                                    [100%]

============================== 44 passed in 3.96s ==============================
```

# Usage without Docker
Step in project folder:
```bash
cd Rover-Takehome-Web/
```
### Run CSV generator
Make sure that the command `python3 --version` in your local outputs this:
```bash
Python 3.6.9
```
Then you can just do:
```bash
make run
```
output:
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
Collecting dataclasses==0.8 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/fe/ca/75fac5856ab5cfa51bbbcefa250182e50441074fdc3f803f6e76451fab43/dataclasses-0.8-py3-none-any.whl
Collecting numpy==1.19.5 (from -r requirements.txt (line 2))
...
Installing collected packages: dataclasses, numpy, six, python-dateutil, pytz, pandas, toml, py, zipp, typing-extensions, importlib-metadata, pyparsing, packaging, iniconfig, pluggy, attrs, pytest, regex, tomli, pathspec, mypy-extensions, typed-ast, appdirs, click, black, isort
Successfully installed appdirs-1.4.4 attrs-21.2.0 black-21.7b0 click-8.0.1 dataclasses-0.8 importlib-metadata-4.6.4 iniconfig-1.1.1 isort-5.9.3 mypy-extensions-0.4.3 numpy-1.19.5 packaging-21.0 pandas-1.1.5 pathspec-0.9.0 pluggy-0.13.1 py-1.10.0 pyparsing-2.4.7 pytest-6.2.4 python-dateutil-2.8.2 pytz-2021.1 regex-2021.8.21 six-1.16.0 toml-0.10.2 tomli-1.2.1 typed-ast-1.4.3 typing-extensions-3.10.0.0 zipp-3.5.0
PYTHONPATH=src venv/bin/python src/main.py --output= --input=
/Users/pablobuenaposada/Desktop/rover/venv/lib/python3.6/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
Reading: reviews.csv
Writing: output/sitters.csv
```
Note that virtual env is getting created (only first time) and used automatically.

Then check inside `output/` folder you should have a file called `sitters.csv`, you might want to delete this file first to just prove that the csv is getting generated after this command since I already deliver one there as asked in the instructions.

```bash
pablobuenaposada$ cat output/sitters_docker.csv
email,name,profile_score,ratings_score,search_score
user7508@t-mobile.com,Leilani R.,1.15,3.5,3.5
user9029@t-mobile.com,Melissa C.,1.35,4.0,2.94
user7903@hotmail.com,Faridah D.,1.15,4.6,2.88
user7650@verizon.net,Robert S.,1.15,3.57,2.85
...
```

Alternatively you can choose source and/or destination csv paths with the following arguments:
```bash
make run output=whatever.csv input=other_source.csv
```
by default output is `output/sitters.csv` and input is `reviews.csv`

### Run tests
```bash
make test
```
output:
```bash
PYTHONPATH=src venv/bin/pytest src/tests
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.6.9, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/pablobuenaposada/Desktop/rover
collected 44 items

src/tests/test_main.py .                                                                                                                                                      [  2%]
src/tests/csv_utils/test_csv_utils.py .......                                                                                                                                 [ 18%]
src/tests/models/test_sitter.py ................................                                                                                                              [ 90%]
src/tests/models/test_sitters.py ....                                                                                                                                         [100%]

================================================================================= warnings summary ==================================================================================
venv/lib/python3.6/site-packages/pandas/compat/__init__.py:120
  /Users/pablobuenaposada/Desktop/rover/venv/lib/python3.6/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
    warnings.warn(msg)

-- Docs: https://docs.pytest.org/en/stable/warnings.html
=========================================================================== 44 passed, 1 warning in 0.93s ===========================================================================
```

# Discussion question
- Describe how you would approach API design for a backend service to provide sitter and rank data to a client/web frontend.
have a `POST` `domain/api/v1/stay` 202
  `GET` `domain/api/v1/sitter/{id}` 200
  `GET` `domain/api/v1/sitter?order=asc` 200 paginated
  
  
  
  
  
