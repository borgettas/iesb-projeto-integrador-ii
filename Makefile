SHELL := /bin/bash

.PHONY: attach
attach: # Create postgres
	docker compose -f docker/postgres/docker-compose.yml up -d