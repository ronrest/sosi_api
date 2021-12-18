# Sosapi

Pronounced *"So-sappy"*.

A simple, base for building REST API client wrappers in Python.


## Installing


```bash
# ------------------------------------------------------------------------------
# 1. INSTALL DEPENDENCIES (only run one of these)
# ------------------------------------------------------------------------------
#    NOTE: Dev dependencies are exactly the same, but with some aditional 
#    packages for running tests, checking formatting of code, etc.
# ------------------------------------------------------------------------------
#    NOTE: the `strict` versions ensure that your virtual environment ONLY has
#    the dependencies listed in the requrements file. Removes everything else.
#    Requires pip-tools to be installed: 
#        pip install pip-tools
# ------------------------------------------------------------------------------
# a. Prod dependencies (compatible with existing virtualenv)
pip install -r requirements.txt

# b. Dev dependencies (compatible with existing virtualenv)
pip install -r requirements-dev.txt

# c. Strict Prod dependencies (Warning: might delete libraries in virtualenv)
pip-sync

# d. Strict Dev dependencies (Warning: might delete libraries in virtualenv)
pip-sync requirements.txt requirements-dev.txt


# ------------------------------------------------------------------------------
# 2. INSTALL PACKAGE (only run one of these)
# ------------------------------------------------------------------------------
# a. Install package regularly
pip install .

# b. Install package in editable mode (for development)
pip install -e .

```


## Extending





## Contributing

### Update dependencies

```bash
# ------------------------------------------------------------------------------
# PREPARE PINNED DEPENDENCIES
# NOTE: Requires `pip-tools` to be installed.
# ------------------------------------------------------------------------------
# 1. Create the requirements.txt file (Prod dependencies)
pip-compile  

# 2. Create requirements-dev.txt (Dev dependencies)
pip-compile setup.py --extra dev -o requirements-dev.txt

```
