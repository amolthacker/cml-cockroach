#!/bin/bash

host=$(hostname -f)

num_nodes=3
start_http_port=9991
start_comm_port=26211

li=$(($num_nodes-1))

jn_str="$host:$start_comm_port"
for (( i=1; i<=$li; i++ ))
do
        jn_str="$jn_str,$host:$(($start_comm_port+$i))"
done

echo "Starting local Cockroach cluster ..."
for (( i=0; i<=$li; i++ ))
do
        comm_port=$(($start_comm_port+$i))
        http_port=$(($start_http_port+$i))
        cockroach start --insecure --store=node$i --listen-addr=$host:$comm_port --http-addr=$host:$http_port --join=$jn_str --background
        sleep 5
done
echo

sleep 5

echo "Initiating Cockroach cluster ..."
cockroach init --insecure --host=$host:$start_comm_port
echo

sleep 10

grep 'node starting' node1/logs/cockroach.log -A 11
echo

cockroach node status --insecure --host $host:$start_comm_port
echo
