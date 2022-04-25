# Deploy PowerAPI with Docker compose
This directory provide configuration files to deploy a PowerAPI monitoring stack on a cluster with docker stack.

The resulting cluster will be composed of:
- A master node that will host the databases, formula and dashboard
- One or several worker nodes that will host one sensor each

## Prerequisites
You will need to ensure you have installed docker: see the [docker documentation](https://docs.docker.com/get-docker/)

## Usage
You will need to first setup a docker **swarm**.

On the master node, initialize the swarm with:
```
docker swarm init --advertise-addr <MASTER IP>
```
Where `<MASTER IP>` must be replaced by the IP address of the master node (note: this address must be reachable by every worker nodes). Once run, this command will output instructions on how to make workers join the swarm. Basically, you will need to run a command on every workers: 
```
docker swarm join --token <TOKEN>
```
Where `<TOKEN>` will be provided in the previously mentionned output.

Then, create the required network used by every deployed services:
```
docker network create --driver overlay --attachable public
```
Then, add the required labels for every nodes (to distinguised master from workers). On the master node, run:
```
docker node update --label-add nodeType=monitoring <MASTER NODE NAME>
```
Then, for every workers, run:
```
docker node update --label-add nodeType=worker <WORKER NODE NAME>
```
You can find the name of every nodes with `docker node ls`.

Your swarm is ready! You can now start PowerAPI. If you don't destroy your swarm, you won't have to run the previous commands again. If however you want to destroy the swarm, you can run `docker swarm leave -f` on every nodes.

To start a PowerAPI stack, run 
```
make start-all
```

To stop the stack, run 
```
make stop-all
```