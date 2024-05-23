SHELL := /bin/bash

.PHONY: up
up:
	docker compose -f docker/docker-compose.yml up

.PHONY: run
run:
	poetry run python app/ingestion/camara.py