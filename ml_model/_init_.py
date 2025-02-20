[tox]
envlist = py311
[testenv]
deps =
 pytest
 scikit-learn
 joblib
 # Install the package in editable mode
 -e .
commands =
 pytest tests/ # Run test cases
[testenv:deploy]
deps =
 scikit-learn
 joblib
commands =
 python deploy.py # Deploy mode 
