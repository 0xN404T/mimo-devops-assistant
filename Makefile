install:
	pip install -r requirements.txt

check:
	python -m py_compile devops_assistant.py

run:
	python devops_assistant.py
