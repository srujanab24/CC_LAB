#!/usr/bin/env bash
# Usage: ./scripts/benchmark.sh type1   (inside the Proxmox VM)
#        ./scripts/benchmark.sh type2   (inside the VMware VM)
set -e
LABEL="${1:?Usage: ./scripts/benchmark.sh <type1|type2>}"
mkdir -p results

command -v sysbench >/dev/null || { sudo apt update && sudo apt install sysbench -y; }

{
  echo "== hostnamectl =="; hostnamectl
  echo "== lscpu =="; lscpu
  echo "== free -h =="; free -h
  echo "== df -h =="; df -h
  echo "== sysbench --version =="; sysbench --version
} > "results/${LABEL}_sysinfo.txt"

sysbench cpu --cpu-max-prime=20000 run | tee "results/${LABEL}.txt"
echo "Saved results/${LABEL}.txt and results/${LABEL}_sysinfo.txt"
