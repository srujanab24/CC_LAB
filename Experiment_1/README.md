
# Experiment 1: Performance Analysis of Type-1 and Type-2 Hypervisors

## 1. Overview

This experiment compares the CPU performance of two virtualization platforms:

- **Proxmox VE** — a Type-1 hypervisor platform.
- **VMware Workstation** — a Type-2 hypervisor application.

Ubuntu virtual machines are used to run the `sysbench` CPU benchmark. The results are recorded and compared to understand how the two virtualization approaches perform.

## 2. Objectives

- Understand Type-1 and Type-2 hypervisors.
- Create and configure Ubuntu virtual machines.
- Execute a CPU benchmark using sysbench.
- Record execution time, events per second, and CPU latency.
- Compare the observed results and discuss the limitations of the experiment.

## 3. Technologies Used

| Component | Technology |
|---|---|
| Type-1 virtualization | Proxmox VE |
| Type-2 virtualization | VMware Workstation |
| Guest operating system | Ubuntu Linux |
| Benchmark tool | sysbench |
| Terminal | Linux terminal |
| Version control | Git and GitHub |

## 4. Experiment Environment

The tests were performed using the same physical computer. The exact host specifications and hypervisor versions should be recorded in the lab report.

### VMware Workstation VM configuration

- Virtual CPUs: 2 processors
- Memory: 2048 MB
- Virtual disk: 20 GB
- Network: NAT
- Guest operating system: Ubuntu

**Note:** Verify the Proxmox VM configuration before claiming that both VMs used identical resources.

## 5. Benchmark Command

The CPU benchmark was executed using sysbench with a prime-number calculation workload.

```bash
sysbench cpu --cpu-max-prime=20000 --threads=1 run
```

The benchmark uses one thread and tests CPU performance by calculating prime numbers up to the configured limit.

## 6. VMware Workstation Results

| Metric | Observed result |
|---|---:|
| sysbench version | 1.0.20 |
| Threads | 1 |
| Prime limit | 20,000 |
| Events per second | 2,436.05 |
| Total execution time | 10.0006 seconds |
| Total events | 24,366 |
| Minimum latency | Approximately 0.40 ms |
| Average latency | 0.41 ms |
| Maximum latency | 4.39 ms |
| 95th percentile latency | 0.42 ms |
| Total latency | 9,992.75 ms |

## 7. Proxmox VE Results

The actual Proxmox benchmark output must be entered here after checking the saved terminal output or screenshot.

| Metric | Result |
|---|---|
| sysbench version | To be verified |
| Threads | To be verified |
| Prime limit | To be verified |
| Events per second | Pending |
| Total execution time | Pending |
| Total events | Pending |
| Average latency | Pending |

Do not estimate or invent missing benchmark values.

## 8. Result Analysis

The events-per-second value indicates how many benchmark events are processed per second. Higher throughput generally indicates better performance for this workload.

Execution time and latency provide additional information about how long the benchmark takes and how long individual events require.

The two platforms should be compared only after confirming that the benchmark command, guest operating system, virtual CPU allocation, memory allocation, and other relevant conditions are comparable.

One benchmark run per platform is not enough to establish a general performance conclusion. Multiple runs and average values would provide a more reliable comparison.

## 9. Screenshots and Evidence

Store the original screenshots and terminal outputs in the experiment's results directory.

Suggested organization:

```text
Experiment_1/
├── README.md
├── LAB_REPORT.md
├── scripts/
└── results/
    ├── Type_1/
    └── Type_2/
```

- `Type_1`: Proxmox VE screenshots and benchmark output.
- `Type_2`: VMware Workstation screenshots and benchmark output.

Use the actual filenames present in the repository when referencing screenshots.

## 10. Conclusion

This experiment demonstrates how a CPU benchmark can be used to observe the performance of virtual machines running on different hypervisor platforms. The recorded results can be compared after confirming that the testing conditions are sufficiently similar.

The final conclusion should be based on the actual measurements collected from both Proxmox VE and VMware Workstation.