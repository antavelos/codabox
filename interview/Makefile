build:
	docker-compose build

up:
	docker-compose up

superuser:
	docker-compose run web python manage.py createsuperuser

migrate:
	docker-compose run web python manage.py migrate

shell:
	docker-compose run web python manage.py shell

collectstatic:
	docker-compose run web python manage.py collectstatic

hello:
	docker-compose run web python manage.py hello_entity ${id}
