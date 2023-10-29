# Contributing

## Update dependencies

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

## (Core developers) Build/Push to pypi

```bash
python -m build
python -m twine upload --repository pypi dist/*

```