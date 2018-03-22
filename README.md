Python3 Unit Test Demo
=========================

How to write and run unit test in python.

- `unittest2` to write and run tests
- `coverage` to generate HTML test report

Install `python3`:

```
brew install python
```

`python3` and `pip3` will be available.

Run:

```
make test
```

Or

```
python3 -m unittest discover -p "test_*.py"
```

Generate HTML Test Report
-------------------------

```
coverage run --source=hello -m unittest discover -p "test_*.py"
coverage html
open htmlcov/index.html
```

