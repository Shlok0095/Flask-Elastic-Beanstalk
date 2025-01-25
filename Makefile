install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203 *.py

test:
	python3 -m pytest test_application.py

deploy:
	eb use flask-demo-environment
	eb deploy

all: install lint test
