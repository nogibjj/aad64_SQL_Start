venv: 
	python3  -m venv ~/.aad64_Individual-Project1

install: 
	pip install --upgrade pip && \
	pip install -r requirements.txt

#create_table:
#  	python database_main.py

test:
#	python -m pytest --nbval-lax *.ipynb
	python -m pytest -vv --cov=main -rw test_*.py

format:
	black *.py

lint:
#	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py

run:
#	python lib.py	
	python main.py

all: venv install lint format test
