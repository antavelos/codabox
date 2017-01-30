# Codabox pre-interview exercise
This exercise demonstrates a simple Django app running in Docker. Moreover a simple Makefile is provided assembling some basic docker and django commands under a common cli which can be used for setting up the environment and the project.

## Specs
* It should expose a web page that display a "Hello [name]" message at the following URL: http://codabox-interview.dev/hello-world/[id] . The [id] should represent a database object containing the [name] part of the "Hello [name]" message.
* It should expose an administration page to create new database objects.
* It should expose a command line application that outputs the "Hello [name]" message. this command line application will take the [id] as a parameter.

## Makefile
The Makefile provides the following commands:
* **`make build`:** It builds the docker containers. Alias of `docker-compose build`.
* **`make up`:** It runs the docker containers. Alias of `docker-compose up -d`.
* **`make stop`:** It stops the docker containers. Alias of `docker-compose stop`.
* **`make superuser`:** It craetes a django super user. Alias of `docker-compose run web python manage.py createsuperuser`.
* **`make migrate`:** It applies the django app migrations. Alias of `docker-compose run web python manage.py createsuperuser`.
* **`make shell`:** It runs the django app shell. Alias of `docker-compose run web python manage.py shell`.
* **`make collectstatic`:** It collects all the static files into static folder. Alias of `docker-compose run web python manage.py collectstatic`.
* **`make hello id=[id]`:** It executes the custom django command hello_entity which accepts one argument. Alias of `docker-compose run web python manage.py hello_entity [id]`.

## Setup
Upon cloning the repository localy follow the below steps in order to set the application up and running:

1. `cd ./codabox/interview`
2. `make build`
3. `make up`

Now the server should be up and running. You can stop it by calling `make stop`.

## Usage
1. In another terminal run `make superuser` in order to create an admin for accesing the admin page
2. Access the admin page by pointing your browser to [http://localhost/admin](http://localhost/admin) and login with the credentials you created. There you can create new entities by giving them a name.
3. Say hello to the entities you just created by pointing your browser to [http://localhost/hello-world/[id]](http://localhost/hello-world/[id]). Replace the [id] with the id of one of the entities you created in the previous step.
4. You can also say hello via the command line by running `make hello id=[id]`.

### Stack
Python 3.5

PostgreSQL 9.6.1

Django 1.10.5

gunicorn 19.6.0

### Environment
The project was tested under `Ubuntu 16.10` with `docker 1.13.0` and `docker-compose 1.10.0`
