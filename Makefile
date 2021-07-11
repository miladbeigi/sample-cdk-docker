build:
	docker-compose build

shell:
	docker-compose run --name cdk-shell --rm cdk bash