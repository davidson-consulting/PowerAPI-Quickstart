#!/usr/bash

start-all: start-monitoring start-power-api

start-monitoring:
	docker stack deploy \
	--compose-file modules/monitoring/monitoring.yml \
	monitoring

start-power-api:
	docker stack deploy \
	--compose-file modules/power-api/power-api.yml \
	power-api

stop-all: stop-monitoring stop-power-api

stop-monitoring:
	docker stack rm monitoring

stop-power-api:
	docker stack rm power-api
