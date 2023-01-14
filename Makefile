VOLUME=$(shell basename $(PWD))

develop: clean build migrations.upgrade run

clean:
	docker-compose rm -vf

build:
	docker-compose build

run:
	docker-compose up

stop: 
	docker-compose stop

frontend-shell:
	docker-compose run frontend \
	  sh

backend-shell:
	docker-compose run worker \
	  sh

python-shell:
	docker-compose run worker \
	  poetry run flask shell