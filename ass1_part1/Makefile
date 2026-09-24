IMAGE ?= ee349-part1
PYTHON ?= python

.PHONY: help test docker-build docker-test verify clean

help:
	@echo "make test          - run pytest locally"
	@echo "make docker-build  - build the Docker image"
	@echo "make docker-test   - run pytest inside Docker"
	@echo "make verify        - all of the above; nonzero exit if anything fails"

test:
	$(PYTHON) -m pytest -q

docker-build:
	docker build -t $(IMAGE) .

docker-test:
	docker run --rm $(IMAGE) python -m pytest -q

verify: test docker-build docker-test
	@echo "VERIFY OK"

clean:
	docker rmi -f $(IMAGE)
