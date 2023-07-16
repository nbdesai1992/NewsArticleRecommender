.PHONY: env activate clean

env:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

activate:
	@echo "Run 'source venv/bin/activate' to activate the virtual environment"

clean:
	# check if the venv is activated
	if [ -n "$$VIRTUAL_ENV" ]; then \
		deactivate; \
	fi
	rm -rf venv