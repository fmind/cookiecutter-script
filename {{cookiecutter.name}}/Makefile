init:
	pip install '.[dist]'
	pip install '.[repl]'
	pip install '.[test]'
	pip install -e .

hook:
	echo "make all" > .git/hooks/pre-commit
	chmod u+x .git/hooks/pre-commit

test:
	pytest --doctest-modules

type:
	pytest --mypy -m mypy

lint:
	pytest --flakes -m flakes

style:
	pytest --black -m black

wheel:
	python setup.py bdist_wheel

upload: wheel
	twine upload -r pypi dist/*.whl

all: type lint test style wheel;
