# Experiment 1: Performance Analysis of Type-1 and Type-2 Hypervisors

![Course](https://img.shields.io/badge/Course-Cloud%20Computing-blue)
![Hypervisors](https://img.shields.io/badge/Hypervisors-Proxmox%20VE%20%7C%20VMware%20Workstation-orange)
![Benchmark](https://img.shields.io/badge/Benchmark-sysbench%20CPU-green)

**Student:** Srujana  
**Institution:** KLE Technological University, Hubballi  
**Course:** Cloud Computing  
**Experiment:** 1 - Type-1 vs Type-2 hypervisor CPU performance

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Objectives](#2-objectives)
3. [Background and Theory](#3-background-and-theory)
4. [Architecture Diagrams](#4-architecture-diagrams)
5. [Experimental Setup](#5-experimental-setup)
6. [Experimental Procedure](#6-experimental-procedure)
7. [Understanding the sysbench Output](#7-understanding-the-sysbench-output)
8. [Results](#8-results)
9. [Graphs and Visualisations](#9-graphs-and-visualisations)
10. [Analysis and Discussion](#10-analysis-and-discussion)
11. [Conclusion](#11-conclusion)
12. [Limitations and Threats to Validity](#12-limitations-and-threats-to-validity)
13. [Troubleshooting](#13-troubleshooting)
14. [Repository Structure](#14-repository-structure)
15. [How to Reproduce](#15-how-to-reproduce)
16. [References](#16-references)

---

## 1. Abstract

This experiment compares the CPU performance of two virtualisation architectures: a **Type-1 (bare-metal) hypervisor, Proxmox VE**, and a **Type-2 (hosted) hypervisor, VMware Workstation**. An identical Ubuntu virtual machine (2 vCPU, 2 GB RAM, 20 GB disk) was created on each platform, and the `sysbench` CPU benchmark (prime-number verification up to 20,000) was run under the same conditions. Throughput (events/sec), total events and latency statistics were collected and compared.

> Fill in one sentence with your headline result after running the experiment, for example: "Type-X achieved N% higher throughput than Type-Y."

---

## 2. Objectives

1. Deploy an Ubuntu VM on a **Type-1** hypervisor (Proxmox VE) and on a **Type-2** hypervisor (VMware Workstation).
2. Give both VMs the **same resources** so the comparison is fair.
3. Run the **`sysbench` CPU benchmark** on both VMs with identical parameters.
4. Collect **throughput and latency** metrics (events/sec, total events, min/avg/95th/max latency).
5. **Explain the differences** using hypervisor architecture (extra software layers, scheduling, memory translation).
6. Recommend which hypervisor type suits which use case.

---

## 3. Background and Theory

### 3.1 What is virtualisation?
Virtualisation lets one physical machine run several isolated virtual machines (VMs). A **hypervisor** (virtual machine monitor) creates the VMs and shares CPU, memory, storage and network among them. It is the foundation of cloud computing, because providers rent out VMs rather than physical servers.

### 3.2 Type-1 hypervisor (bare-metal)
A Type-1 hypervisor runs **directly on the hardware** with no general-purpose desktop OS beneath it. Examples: Proxmox VE (Linux KVM), VMware ESXi, Microsoft Hyper-V, Xen.
- Fewer layers between the guest and the CPU.
- Used in data centres and production cloud environments.
- Guest CPU instructions run on hardware virtualisation extensions (Intel VT-x / AMD-V) with minimal interception.

### 3.3 Type-2 hypervisor (hosted)
A Type-2 hypervisor runs **as an application on top of a host OS**. Examples: VMware Workstation, Oracle VirtualBox.
- Easy to install on a laptop or desktop.
- The guest depends on the host OS for scheduling, memory and I/O.
- Host background activity (antivirus, updates, other apps) can compete with the VM for CPU time.

### 3.4 Comparison at a glance

| Aspect | Type-1 (Bare-metal) | Type-2 (Hosted) |
|---|---|---|
| Runs on | Physical hardware directly | A host operating system |
| Examples | Proxmox VE, ESXi, Hyper-V, Xen | VMware Workstation, VirtualBox |
| Layers between VM and hardware | Fewer | More (host OS + hypervisor app) |
| Typical performance | Higher, more predictable | Slightly lower, more variable |
| Typical use | Data centres, cloud, production | Development, testing, learning |
| Management | Web UI / CLI, server-oriented | Desktop GUI |
| Resource contention | Only between VMs | VMs plus host OS and its apps |

### 3.5 About the benchmark
`sysbench cpu` checks every number from 2 up to `--cpu-max-prime` for primality using integer arithmetic. It is **CPU-bound**: it barely uses disk or network, so it isolates how efficiently the hypervisor lets the guest use the processor. One **event** is one complete pass over the prime search.

---

## 4. Architecture Diagrams

![Architecture comparison](images/architecture_comparison.png)

| Type-1 (Proxmox VE) | Type-2 (VMware Workstation) |
|---|---|
| ![Type 1](images/architecture_type1.png) | ![Type 2](images/architecture_type2.png) |

The Type-2 stack has one extra layer (the host OS) between the VM and the hardware.

---

## 5. Experimental Setup

### 5.1 Virtual machine specification

Both VMs use the same resources. Replace the `<...>` values with your own.

| Parameter | Type-1: Proxmox VE | Type-2: VMware Workstation |
|---|---|---|
| VM name | `<vm-name-type1>` | `<vm-name-type2>` |
| Guest OS | `<Ubuntu version>` | `<Ubuntu version>` |
| vCPU | 2 (1 socket, 2 cores) | 2 (1 processor, 2 cores) |
| RAM | 2048 MB | 2048 MB |
| Virtual disk | 20 GB | 20 GB |
| Network | `<e.g. VirtIO bridge>` | `<e.g. NAT>` |
| Host OS | Proxmox VE (Debian-based) | `<Windows version>` |
| Host CPU model | `<your CPU>` | `<your CPU>` |
| sysbench version | `<output of sysbench --version>` | `<output of sysbench --version>` |

### 5.2 Benchmark parameters

| Parameter | Value |
|---|---|
| Tool | `sysbench cpu` |
| `--cpu-max-prime` | 20000 |
| Threads | 1 (default) |
| Duration | 10 seconds (default) |
| Runs | `<number of runs>` |

### 5.3 Fairness checklist
- [ ] Same vCPU, RAM and disk size on both VMs
- [ ] Same Ubuntu version and same sysbench version
- [ ] No other heavy programs running during the test
- [ ] Same benchmark command on both VMs
- [ ] Each test repeated at least 3 times (record the best or the average and say which)

---

## 6. Experimental Procedure

![Experiment workflow](images/experiment_workflow.png)

### Step 1: Create the VM on Proxmox VE (Type-1)
1. Log in to the Proxmox web console (`https://<proxmox-ip>:8006`).
2. Click **Create VM**.
3. **General:** give the VM an ID and name.
4. **OS:** select the Ubuntu ISO.
5. **System:** keep the defaults.
6. **Disk:** set 20 GB.
7. **CPU:** 1 socket, 2 cores.
8. **Memory:** 2048 MB.
9. **Network:** choose the default bridge (`vmbr0`).
10. Finish, start the VM and install Ubuntu.

### Step 2: Create the VM on VMware Workstation (Type-2)
1. Open VMware Workstation and choose **Create a New Virtual Machine**, then **Typical**.
2. Select the same Ubuntu ISO and name the VM.
3. Set disk size to 20 GB.
4. Customise hardware: 2 GB memory, 1 processor with 2 cores, NAT network.
5. Finish, start the VM and install Ubuntu.

### Step 3: Verify the configuration (on both VMs)
```bash
hostnamectl     # OS, kernel, hostname, virtualisation type
lscpu           # CPU count, model, virtualisation info
free -h         # memory
df -h           # disk
top             # confirm the system is idle
```
Take a screenshot of these outputs for each VM.

### Step 4: Install sysbench (on both VMs)
```bash
sudo apt update
sudo apt install sysbench -y
sysbench --version
```

### Step 5: Run the benchmark (on both VMs)
```bash
sysbench cpu --cpu-max-prime=20000 run
```
Or use the helper script, which also saves system info and output files:
```bash
./scripts/benchmark.sh type1     # inside the Proxmox VM
./scripts/benchmark.sh type2     # inside the VMware VM
```
Save screenshots as `images/1.png` (Type-1) and `images/2.png` (Type-2).

### Step 6: Process the results (on your PC)
Copy `type1.txt` and `type2.txt` into the `results/` folder, then:
```bash
pip install matplotlib
python scripts/parse_sysbench.py
python scripts/generate_plots.py
python scripts/update_readme.py
```

---

## 7. Understanding the sysbench Output

| Field | Meaning | Better |
|---|---|---|
| `events per second` | Throughput: prime searches completed per second | Higher |
| `total time` | Wall-clock time of the run (about 10 s) | n/a |
| `total number of events` | Number of prime searches finished in the window | Higher |
| `latency min` | Fastest single event | Lower |
| `latency avg` | Mean event time | Lower |
| `latency 95th percentile` | 95% of events finished faster than this | Lower |
| `latency max` | Slowest single event (shows scheduling spikes) | Lower |

Relationship: `events per second = total events / total time`.

The **95th percentile** and **max** latency show how *consistent* performance is. A hypervisor can have a good average but bad spikes if the host scheduler interrupts the VM.

### Screenshots

| Type-1 (Proxmox VE) | Type-2 (VMware Workstation) |
|---|---|
| ![Type 1 output](images/1.png) | ![Type 2 output](images/2.png) |

---

## 8. Results

<!-- RESULTS_START -->
_Run `python scripts/update_readme.py` after collecting your results and this table will be filled in automatically._
<!-- RESULTS_END -->

Formulas used for the difference column:

- Throughput and total events: `(Type-1 - Type-2) / Type-2 x 100`
- Latency: `(Type-1 - Type-2) / Type-2 x 100` (a negative value means Type-1 has lower latency)

Raw outputs are stored in [`results/`](results/).

---

## 9. Graphs and Visualisations

### Chart 1: CPU throughput (events per second)
![Throughput](images/events_per_second_comparison.png)

### Chart 2: Total events processed
![Total events](images/total_events_comparison.png)

### Chart 3: Latency comparison (min, avg, 95th percentile, max)
![Latency](images/latency_comparison.png)

### Chart 4: Percentage advantage of Type-1 over Type-2
![Delta](images/performance_delta.png)

### Chart 5: Overall dashboard
![Dashboard](images/overall_performance_dashboard.png)

---

## 10. Analysis and Discussion

> Write this section in your own words using your measured numbers. Suggested structure:

**10.1 Throughput.** Which hypervisor processed more events per second, and by what percentage?

**10.2 Latency and consistency.** Compare average, 95th percentile and max latency. Which platform was more consistent?

**10.3 Why might the results differ?** Discuss, with reference to your data:
- **Extra layers in Type-2.** Guest requests pass through the VMM and the host OS before reaching the hardware.
- **Host OS scheduling.** The host OS scheduler (for example Windows) may pause VM threads to run other processes, causing latency spikes.
- **Background activity.** Antivirus, updates and desktop services share the CPU in a Type-2 setup.
- **Hardware virtualisation.** Both use VT-x/AMD-V, so for pure CPU work the gap is usually small, and results depend on the host machine.
- **Memory translation.** Nested/extended page tables and the host memory manager affect memory-heavy work more than this CPU test.

**10.4 Do the results match theory?** Say whether Type-1 was faster, and if the result surprised you, explain possible reasons (different hosts, power settings, thermal throttling, number of runs).

---

## 11. Conclusion

> Summarise in 4-6 lines: which hypervisor performed better on this CPU benchmark, by how much, and why. Then give use-case guidance:

- **Type-1 (Proxmox VE, ESXi, KVM):** production servers, cloud data centres, databases, workloads needing predictable latency.
- **Type-2 (VMware Workstation, VirtualBox):** development, testing, learning labs, running a second OS on a personal computer.

---

## 12. Limitations and Threats to Validity

- **Different physical hosts.** If Proxmox and VMware ran on different machines, hardware differences affect the comparison more than the hypervisor does. State clearly what host each used.
- **Single benchmark.** `sysbench cpu` measures only CPU integer work, not disk, memory or network performance.
- **Small number of runs.** Repeat several times and report the average or best run.
- **Background load.** Other host activity can change results between runs.
- **CPU model exposure.** Different virtual CPU types can change performance slightly.

Possible extensions: `sysbench memory`, `sysbench fileio`, multi-thread runs (`--threads=2`), and `iperf3` for network throughput.

---

## 13. Troubleshooting

| Problem | Fix |
|---|---|
| `sysbench: command not found` | `sudo apt update && sudo apt install sysbench -y` |
| VMware says VT-x is not available | Enable virtualisation in BIOS/UEFI and turn off conflicting Hyper-V features if needed |
| Proxmox VM will not boot the ISO | Check the ISO is attached and boot order lists CD/DVD first |
| Results vary a lot between runs | Close other applications, plug in power, run 3 or more times |
| `python scripts/...` fails with import error | `pip install matplotlib` |
| Images not showing in README | Make sure the files exist in `images/` with the exact names |
| `parse_sysbench.py` cannot find a field | Check `results/type1.txt` and `type2.txt` contain the full sysbench output |

---

## 14. Repository Structure

```
Experiment_1/
├── README.md                     # This report
├── LAB_REPORT.md                 # Formal lab report template
├── images/
│   ├── 1.png                     # Proxmox sysbench screenshot (add yours)
│   ├── 2.png                     # VMware sysbench screenshot (add yours)
│   ├── architecture_type1.png
│   ├── architecture_type2.png
│   ├── architecture_comparison.png
│   ├── experiment_workflow.png
│   ├── events_per_second_comparison.png
│   ├── total_events_comparison.png
│   ├── latency_comparison.png
│   ├── performance_delta.png
│   └── overall_performance_dashboard.png
├── results/
│   ├── type1.txt / type2.txt     # Raw sysbench output
│   ├── *_sysinfo.txt             # System info captured per VM
│   └── summary.json              # Parsed numbers
└── scripts/
    ├── benchmark.sh              # Run and save the benchmark
    ├── parse_sysbench.py         # Parse output to JSON
    ├── generate_diagrams.py      # Architecture and workflow diagrams
    ├── generate_plots.py         # Result charts
    └── update_readme.py          # Fill the results table
```

---

## 15. How to Reproduce

```bash
# Inside each VM
sudo apt update && sudo apt install sysbench -y
./scripts/benchmark.sh type1      # or type2

# On your computer
pip install matplotlib
python scripts/generate_diagrams.py
python scripts/parse_sysbench.py
python scripts/generate_plots.py
python scripts/update_readme.py
```

---

## 16. References

1. sysbench project: https://github.com/akopytov/sysbench
2. Proxmox VE documentation: https://pve.proxmox.com/pve-docs/
3. VMware Workstation documentation: https://docs.vmware.com/
4. Popek, G. and Goldberg, R. (1974). Formal requirements for virtualizable third generation architectures. *Communications of the ACM*.
5. Course notes and lab manual, Cloud Computing, KLE Technological University.
