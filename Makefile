SHELL := /bin/bash

.PHONY: attach
attach:
	docker compose -f docker/postgres/docker-compose.yml up -d


.PHONY: run
run:
	poetry run python app/ingestion/deputados.py