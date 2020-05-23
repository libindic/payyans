test:
	coverage run --source=libindic -m unittest discover -s libindic

flake:
	flake8 --max-complexity 10 libindic

travis: test flake

clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	rm -rf build dist *egg* .tox .coverage .testrepository
