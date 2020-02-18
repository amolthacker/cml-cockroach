#!/bin/bash

version="19.2.4"
wget -qO- https://binaries.cockroachdb.com/cockroach-v$version.linux-amd64.tgz | tar  xvz

sudo cp -i cockroach-v$version.linux-amd64/cockroach /usr/local/sbin/
