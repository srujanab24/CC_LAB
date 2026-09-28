# Lab Report: Experiment 1
## Performance Analysis of Type-1 and Type-2 Hypervisors

| | |
|---|---|
| **Name** | Srujana |
| **USN** | `<your USN>` |
| **Institution** | KLE Technological University, Hubballi |
| **Course** | Cloud Computing |
| **Date of experiment** | `<date>` |
| **Date of submission** | `<date>` |

---

## 1. Aim
To compare the CPU performance of a Type-1 hypervisor (Proxmox VE) and a Type-2 hypervisor (VMware Workstation) using the sysbench CPU benchmark.

## 2. Objectives
1. Create identical Ubuntu VMs on both hypervisors.
2. Run the sysbench CPU test with the same parameters.
3. Compare throughput and latency.
4. Explain the differences using hypervisor architecture.

## 3. Theory
_Explain in your own words:_ what a hypervisor is; Type-1 vs Type-2 (with a diagram, see `images/architecture_comparison.png`); hardware virtualisation (VT-x / AMD-V); why a CPU benchmark is used.

## 4. Requirements

| Item | Details |
|---|---|
| Physical host (CPU, RAM) | `<fill>` |
| Host OS for VMware | `<fill>` |
| Proxmox VE version | `<fill>` |
| VMware Workstation version | `<fill>` |
| Guest OS | `<Ubuntu version>` |
| Benchmark tool | sysbench `<version>` |

## 5. VM Configuration

| Parameter | Type-1 | Type-2 |
|---|---|---|
| vCPU | 2 | 2 |
| RAM | 2 GB | 2 GB |
| Disk | 20 GB | 20 GB |

_Insert configuration screenshots._

## 6. Procedure
1. Created the VM on Proxmox VE.
2. Created the VM on VMware Workstation.
3. Verified configuration with `hostnamectl`, `lscpu`, `free -h`, `df -h`.
4. Installed sysbench with `sudo apt install sysbench -y`.
5. Ran `sysbench cpu --cpu-max-prime=20000 run` on both VMs.
6. Recorded and compared the results.

## 7. Observations

_Insert screenshots `images/1.png` and `images/2.png`, then the results table from the README._

## 8. Graphs
_Insert the charts from `images/` and add a one-line caption for each._

## 9. Result Analysis
_Compare throughput, total events and latency. State which hypervisor performed better and by what percentage._

## 10. Discussion
_Explain the reasons using the architecture: number of layers, host OS scheduling, background processes, hardware virtualisation._

## 11. Conclusion
_4-6 lines._

## 12. Viva Questions (practice)
1. What is the difference between Type-1 and Type-2 hypervisors?
2. Why is Type-1 preferred in cloud data centres?
3. What does the 95th percentile latency tell you that the average does not?
4. What is Intel VT-x / AMD-V?
5. Why do we give both VMs identical resources?
6. Name two other benchmarks you could use (memory, disk, network).

## 13. References
_List the documentation and books you used._
