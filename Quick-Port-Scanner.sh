#!/bin/bash
# Usage: ./ctf_scan.sh <IP>
for port in {1..65535}; do
  (echo >/dev/tcp/$1/$port) 2>/dev/null && echo "Port $port OPEN"
done
