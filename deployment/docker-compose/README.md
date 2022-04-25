# Deploy PowerAPI with Docker compose
This directory provide configuration files to deploy a PowerAPI monitoring stack on a single server with docker-compose.

## Prerequisites
You will need to ensure you have installed:
- Docker: see the [docker documentation](https://docs.docker.com/get-docker/)
- Docker compose: see the [docker compose documentation](https://docs.docker.com/compose/install/)

## Usage
To start a PowerAPI monitoring stack without a dashboard, run: 
```
docker-compose up -d
```

To start a PowerAPI monitoring stack with a dashboard, run: 
```
docker-compose -f docker-compose.yaml docker-compose.dashboard.yaml up -d
```