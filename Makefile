.DEFAULT_GOAL := help

.PHONY: help validate-docs validate-local selfcheck-validators ci-check validate-csv validate-links validate-workflow validate-all quick-check standard-check full-check

help:
	@echo "Available targets:"
	@echo "  make validate-docs   Run documentation and CSV validation checks"
	@echo "  make validate-local  Run validate-docs and pre-commit if available"
	@echo "  make selfcheck-validators  Run negative-case self-checks for validators"
	@echo "  make validate-csv  Run backlog CSV validator only"
	@echo "  make validate-links  Run markdown local-reference validator only"
	@echo "  make validate-workflow  Run workflow consistency validator only"
	@echo "  make ci-check  Run validate-docs + validator self-checks"
	@echo "  make quick-check  Fast path: CSV + links"
	@echo "  make standard-check  Standard path: validate-docs"
	@echo "  make full-check  Full path: ci-check"

validate-docs:
	python scripts/validate_docs.py

validate-csv:
	python scripts/validate_backlog_csv.py

validate-links:
	python scripts/validate_doc_links.py

validate-workflow:
	python scripts/validate_workflow_consistency.py

validate-local: validate-docs
	@if command -v pre-commit >/dev/null 2>&1; then \
		echo "[INFO] pre-commit found, running pre-commit --all-files"; \
		pre-commit run --all-files; \
	else \
		echo "[WARN] pre-commit not installed; skipped."; \
	fi

selfcheck-validators:
	python scripts/selfcheck_validators.py

ci-check: validate-docs selfcheck-validators
	@echo "[OK] CI check suite completed."

validate-all: ci-check
	@echo "[OK] validate-all completed."

quick-check: validate-csv validate-links
	@echo "[OK] quick-check completed."

standard-check: validate-docs
	@echo "[OK] standard-check completed."

full-check: ci-check
	@echo "[OK] full-check completed."

install:
	python -m pip install -e .

run:
	python scripts/run_all_checks.py
