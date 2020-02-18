#!/bin/bash

host=$(hostname -f)

http_port=9991
comm_port=26211

echo "Starting single node Cockroach ..."
cockroach start-single-node --insecure --listen-addr=$host:$comm_port --http-addr=$host:$http_port --background
echo
