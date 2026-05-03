.PHONY: dev test compose-up compose-down compose-build logs logs-api logs-db logs-redis test-docker shell-api shell-db redis-ping db-psql migration migrate prod-like-up prod-like-up-d prod-like-down prod-like-logs prod-like-migrate prod-like-ps minio-logs minio-console

dev:
	uvicorn app.main:app --reload

test:
	pytest

compose-up:
	docker compose up --build

compose-up-d:
	docker compose up -d --build

compose-down:
	docker compose down

compose-build:
	docker compose build

logs:
	docker compose logs -f

logs-api:
	docker compose logs -f api

logs-db:
	docker compose logs -f postgres

logs-redis:
	docker compose logs -f redis

test-docker:
	docker compose run --rm api pytest

shell-api:
	docker exec -it financial-rag-api bash

shell-db:
	docker exec -it financial-rag-postgres bash

db-psql:
	docker exec -it financial-rag-postgres psql -U ai_backend_user -d ai_backend_foundation

redis-ping:
	docker exec -it financial-rag-redis redis-cli ping

migration:
	docker compose run --rm api alembic revision --autogenerate -m "$(msg)"

migrate:
	docker compose run --rm api alembic upgrade head

prod-like-up:
	docker compose -f docker-compose.prod-like.yml up --build

prod-like-up-d:
	docker compose -f docker-compose.prod-like.yml up -d --build

prod-like-down:
	docker compose -f docker-compose.prod-like.yml down

prod-like-logs:
	docker compose -f docker-compose.prod-like.yml logs -f

prod-like-migrate:
	docker compose -f docker-compose.prod-like.yml run --rm api alembic upgrade head

prod-like-ps:
	docker compose -f docker-compose.prod-like.yml ps

minio-logs:
	docker compose logs -f minio

minio-console:
	@echo "MinIO Console: http://127.0.0.1:9001"
	@echo "Username: minioadmin"
	@echo "Password: minioadmin"