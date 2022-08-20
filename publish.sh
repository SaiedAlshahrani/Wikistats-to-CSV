python setup.py sdist
pip install -q twine
twine upload dist/*
