SHELL := bash

VENV=.venv
VENV_BIN="${VENV}/bin"

BUILD_SOURCEVERSION ?= $(shell git rev-parse HEAD~0)

env:
	@echo "Creating environment..."
	python3 -m venv ${VENV}
	@echo "To activate environment please use: source .venv/bin/activate"
	@echo "Following activation, deactivate command will be made available"
upgrade_pip:
	@echo "Updating pip..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ${VENV_BIN}/python3 -m pip install --upgrade pip ; \
	)
install:
	@echo "Installing dependencies..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ${VENV_BIN}/python3 -m pip install wheel; \
	  ${VENV_BIN}/python3 -m pip install -r $(requirements_file); \
	)
freeze: 
	@echo "Printing venv dependencies (use for debugging)..."
	( \
		. ${VENV_BIN}/activate ; \
		${VENV_BIN}/python3 -m pip freeze ; \
	)
pip_config: 
	@echo "Printing pip configuration (use for debugging)..."
	( \
	  . ${VENV_BIN}/activate ; \
	  echo "Running: pip config list -v" ; \
	  ${VENV_BIN}/python3 -m pip config list -v; \
	)
precommit:
	@echo "Preparing pre-commit for your machine..."
	pre-commit install
run_pytest:
	@echo "Running pytest..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ${VENV_BIN}/python3 -m pytest $(extra_opts) --doctest-modules --junitxml=junit/test-results.xml $(test_folder) ; \
	)
run_pytest_with_coverage:
	@echo "Running pytest with coverage..."
	( \
	  . ${VENV_BIN}/activate ; \
      cov_opts=() ; \
      for elem in $(coverage_folder); do \
        cov_opts+=( --cov=$${elem} ) ; \
      done ; \
      echo "cov_opts: $${cov_opts[@]}" ; \
	  ${VENV_BIN}/python3 -m pytest $(extra_opts) --doctest-modules --junitxml=junit/test-results.xml \
        $${cov_opts[@]} --cov-report=xml --cov-report=html $(test_folder) ; \
	)
run_dynaconf_pytest:
	@echo "Running pytest using dynaconf..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ENV_FOR_DYNACONF=$(dynaconf_env) ${VENV_BIN}/python3 -m pytest $(extra_opts) --doctest-modules --junitxml=junit/test-results.xml $(test_folder) ; \
	)
run_dynaconf_pytest_with_coverage:
	@echo "Running pytest with coverage using dynaconf..."
	( \
	  . ${VENV_BIN}/activate ; \
      cov_opts=() ; \
      for elem in $(coverage_folder); do \
        cov_opts+=( --cov=$${elem} ) ; \
      done ; \
      echo "cov_opts: $${cov_opts[@]}" ; \
	  ENV_FOR_DYNACONF=$(dynaconf_env) ${VENV_BIN}/python3 -m pytest $(extra_opts) --doctest-modules --junitxml=junit/test-results.xml \
	    $${cov_opts[@]} --cov-report=xml --cov-report=html $(test_folder) ; \
	)
lint:
	@echo "Testing code style (PEP8) and running Linter..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ${VENV_BIN}/python3 -m pylint $(lint_folder) ; \
	)
package_wheel:
	@echo "Package project to wheel..."
	( \
	  . ${VENV_BIN}/activate ; \
	  ${VENV_BIN}/python3 -m pip install wheel; \
	  ${VENV_BIN}/python3 setup.py bdist_wheel; \
	)
clean:
	@rm -rf htmlcov junit perf docs/api/_build
	@rm -rf .pytest_cache
	@rm -rf coverage.xml test-output.xml
	@rm -rf .coverage
	@find . -name '__pycache__' -exec rm -rf {} +
	@clear
