
# Lab Report: Experiment 1

## Performance Analysis of Type-1 and Type-2 Hypervisors

| Field | Details |
|---|---|
| Name | Srujana Babannavar |
| USN | Enter your USN |
| Institution | KLE Technological University, Hubballi |
| Department | Computer Science and Engineering (AI) |
| Course | Cloud Computing |
| Date of experiment | Enter experiment date |
| Date of submission | Enter submission date |

---

## 1. Aim

To compare the CPU performance of a Type-1 hypervisor platform, Proxmox VE, and a Type-2 hypervisor application, VMware Workstation, using the sysbench CPU benchmark.

## 2. Objectives

1. Understand the concepts of virtualization and hypervisors.
2. Configure Ubuntu virtual machines on Proxmox VE and VMware Workstation.
3. Execute the same CPU benchmark command on both platforms.
4. Record benchmark metrics such as events per second, execution time, and latency.
5. Compare the observed measurements and identify factors that may affect performance.

## 3. Introduction

Virtualization is a technology that allows multiple virtual machines to run on a physical computer. Each virtual machine can have its own operating system and allocated virtual resources, including CPU, memory, storage, and networking.

A hypervisor is the software layer responsible for creating and managing virtual machines. It allocates physical resources to virtual machines and provides isolation between them.

Virtualization is widely used in cloud computing because it allows hardware resources to be shared among multiple workloads. It can improve resource utilization, simplify management, and support flexible deployment of computing environments.

This experiment uses a CPU benchmark to observe the performance of virtual machines running on two virtualization platforms.

## 4. Theory

### 4.1 Virtualization

Virtualization creates a software-based version of computing resources. Instead of requiring a separate physical computer for every operating system, several virtual machines can share the same physical hardware.

Each virtual machine receives allocated resources and runs independently from the other virtual machines.

### 4.2 Type-1 Hypervisor

A Type-1 hypervisor, also called a bare-metal hypervisor, runs directly on the physical hardware rather than as an ordinary application inside a general-purpose host operating system.

Proxmox VE is a virtualization platform built around Linux-based virtualization technologies. It uses KVM for virtual machines and also supports LXC containers.

**Advantages:**

- Designed for server virtualization.
- Provides centralized virtual machine management.
- Supports resource allocation and monitoring.
- Suitable for virtualization labs and server environments.

### 4.3 Type-2 Hypervisor

A Type-2 hypervisor runs as an application on a host operating system.

VMware Workstation is an example of this approach. It allows users to create and run virtual machines from a desktop operating system.

**Advantages:**

- Convenient for desktop-based experimentation.
- Supports multiple guest operating systems.
- Useful for software development and testing.
- Allows virtual machines to run alongside normal desktop applications.

### 4.4 Difference Between Type-1 and Type-2 Hypervisors

| Feature | Type-1 | Type-2 |
|---|---|---|
| General architecture | Runs directly on physical hardware | Runs as an application on a host OS |
| Example used | Proxmox VE | VMware Workstation |
| Typical use | Server and lab virtualization | Desktop development and testing |
| Host OS relationship | Hypervisor platform manages hardware resources | Depends on the host operating system |
| Performance factors | Hardware, configuration, workload, and virtualization overhead | Hardware, host OS, configuration, workload, and virtualization overhead |

Actual performance depends on the hardware, software versions, VM configuration, and workload. A Type-1 hypervisor should not automatically be assumed to outperform a Type-2 hypervisor in every situation.

## 5. Software and Hardware Requirements

### 5.1 Software Requirements

- Proxmox VE.
- VMware Workstation.
- Ubuntu guest operating system.
- sysbench CPU benchmarking utility.
- Terminal or command-line access.

### 5.2 Hardware Requirements

- A physical computer that supports virtualization.
- Sufficient CPU cores and memory to run the virtual machines.
- Sufficient storage for the hypervisor environment and virtual disks.

### 5.3 Environment Details

Fill in the actual details used during the experiment.

| Parameter | Details |
|---|---|
| Physical computer model | Enter actual model |
| Physical CPU | Enter actual processor |
| Physical RAM | Enter actual memory |
| Host operating system | Enter host OS and version |
| Proxmox VE version | Verify and enter version |
| VMware Workstation version | Verify and enter version |
| Ubuntu version | Verify guest version |
| sysbench version | 1.0.20 reported for VMware |

## 6. Virtual Machine Configuration

### 6.1 VMware Workstation Configuration

The recorded VMware Workstation virtual machine configuration was:

| Parameter | Configuration |
|---|---|
| Guest operating system | Ubuntu |
| Virtual processors | 2 processors |
| Memory | 2048 MB |
| Virtual disk | 20 GB |
| Network mode | NAT |

### 6.2 Proxmox VE Configuration

Enter the actual values from the Proxmox virtual machine configuration.

| Parameter | Configuration |
|---|---|
| Guest operating system | Verify Ubuntu version |
| Virtual CPUs | Verify from VM configuration |
| Memory | Verify from VM configuration |
| Virtual disk | Verify from VM configuration |
| Network configuration | Verify from VM configuration |

For a fair comparison, use the same virtual CPU count, memory allocation, guest OS, and benchmark parameters wherever possible. If the configurations differ, clearly mention the differences when analyzing the results.

## 7. Procedure

### 7.1 Setting Up the Virtual Machines

1. Start the Proxmox VE environment.
2. Create or open the Ubuntu virtual machine.
3. Verify its virtual CPU, memory, and storage allocation.
4. Start the virtual machine and open its terminal.
5. Repeat the configuration check for the Ubuntu virtual machine in VMware Workstation.
6. Record any differences between the two configurations.

### 7.2 Installing sysbench

On each Ubuntu virtual machine, update the package list:

```bash
sudo apt update
```

Install sysbench:

```bash
sudo apt install sysbench
```

Verify the installation:

```bash
sysbench --version
```

Record the version reported by each virtual machine.

### 7.3 Running the CPU Benchmark

Run the following command inside each Ubuntu virtual machine:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=1 run
```

The command uses one thread and a prime-number calculation workload with a maximum prime limit of 20,000.

Record the output, including:

- Events per second.
- Total execution time.
- Total number of events.
- Minimum latency.
- Average latency.
- Maximum latency.
- 95th percentile latency.

Keep the benchmark parameters identical for both platforms.

### 7.4 Recording the Results

1. Save the terminal output or take a screenshot of the results.
2. Record the measured values in the observation tables.
3. Repeat the test several times if possible.
4. Compare the results only after checking that the testing conditions are comparable.

## 8. Observations and Results

### 8.1 VMware Workstation Benchmark

The following values were recorded from the VMware Workstation benchmark output.

| Metric | Observed value |
|---|---:|
| sysbench version | 1.0.20 |
| Number of threads | 1 |
| Maximum prime limit | 20,000 |
| Events per second | 2,436.05 |
| Total execution time | 10.0006 seconds |
| Total events | 24,366 |
| Minimum latency | Approximately 0.40 ms |
| Average latency | 0.41 ms |
| Maximum latency | 4.39 ms |
| 95th percentile latency | 0.42 ms |
| Total latency | 9,992.75 ms |

These values describe the recorded VMware run. They should not be interpreted as universal performance values for VMware Workstation.

### 8.2 Proxmox VE Benchmark

The actual Proxmox benchmark output has not yet been verified in this report. Enter the values from the saved benchmark output or screenshot.

| Metric | Observed value |
|---|---|
| sysbench version | To be verified |
| Number of threads | To be verified |
| Maximum prime limit | To be verified |
| Events per second | Pending measurement |
| Total execution time | Pending measurement |
| Total events | Pending measurement |
| Minimum latency | Pending measurement |
| Average latency | Pending measurement |
| Maximum latency | Pending measurement |
| 95th percentile latency | Pending measurement |

Do not fill this table with estimated or invented measurements.

### 8.3 Comparison Table

Complete this table after obtaining the actual Proxmox measurements.

| Metric | Proxmox VE | VMware Workstation |
|---|---|---|
| sysbench version | Verify | 1.0.20 |
| Threads | Verify | 1 |
| Prime limit | Verify | 20,000 |
| Events per second | Pending | 2,436.05 |
| Total execution time | Pending | 10.0006 seconds |
| Average latency | Pending | 0.41 ms |

## 9. Analysis and Discussion

### 9.1 Events Per Second

Events per second represents the number of benchmark events processed during one second.

A higher events-per-second value generally indicates better throughput for this particular CPU workload, provided the benchmark settings and conditions are comparable.

The VMware Workstation run recorded 2,436.05 events per second. The Proxmox result must be measured before a numerical comparison can be made.

### 9.2 Execution Time

Execution time represents the total time taken by the benchmark.

When the workload and test duration are comparable, lower execution time can indicate better performance. However, results must be interpreted in the context of the benchmark configuration and measurement method.

### 9.3 Latency

Latency represents the time required to process an individual benchmark event.

The recorded VMware average latency was 0.41 ms. The maximum latency was 4.39 ms, showing that some events took longer than the average.

Latency can be affected by CPU scheduling, background processes, host load, and virtual machine configuration.

### 9.4 Factors Affecting Performance

Several factors can affect the benchmark results:

1. Physical CPU architecture and clock speed.
2. Number of virtual CPUs allocated to each VM.
3. Memory allocation.
4. Host operating system activity.
5. Hypervisor and virtualization configuration.
6. Guest operating system and software versions.
7. Background processes running during the benchmark.
8. CPU scheduling and virtualization overhead.
9. Number of repeated runs and measurement variation.

### 9.5 Limitations

This experiment has several limitations:

- Only one benchmark run per platform was recorded.
- The actual Proxmox benchmark values must be verified.
- Identical VM resource allocation has not yet been confirmed.
- A CPU benchmark does not measure all aspects of virtualization performance.
- Results from one physical computer may not generalize to other systems.

Multiple runs and average measurements would improve the reliability of the comparison.

## 10. Result

The CPU benchmark was executed on the VMware Workstation Ubuntu virtual machine, recording 2,436.05 events per second and a total execution time of 10.0006 seconds.

A complete numerical comparison with Proxmox VE requires the actual Proxmox benchmark measurements and verification of the VM configurations. Therefore, no claim that one platform performed better is made until the missing measurements are available.

## 11. Conclusion

This experiment demonstrates the use of sysbench to observe CPU performance in virtual machines running on Proxmox VE and VMware Workstation.

The experiment helps explain the differences between Type-1 and Type-2 virtualization approaches and shows how metrics such as events per second, execution time, and latency can be used to analyze performance.

A reliable comparison requires consistent benchmark parameters, verified virtual machine configurations, and actual measurements from both platforms. Repeated benchmark runs would provide a stronger basis for drawing conclusions.

## 12. Viva Questions and Answers

### Q1. What is virtualization?

Virtualization is a technology that allows multiple virtual machines to share the resources of a physical computer.

### Q2. What is a hypervisor?

A hypervisor is a software layer that creates, runs, and manages virtual machines.

### Q3. What is a Type-1 hypervisor?

A Type-1 hypervisor runs directly on physical hardware. Proxmox VE is the Type-1 virtualization platform used in this experiment.

### Q4. What is a Type-2 hypervisor?

A Type-2 hypervisor runs as an application on a host operating system. VMware Workstation is used as the Type-2 platform in this experiment.

### Q5. What is sysbench?

sysbench is a benchmarking tool used to evaluate system performance through workloads such as CPU and memory tests.

### Q6. What does the CPU benchmark measure?

It measures performance for a specified CPU workload and reports values such as events per second, execution time, and latency.

### Q7. What does events per second mean?

It indicates how many benchmark events are processed per second. Higher throughput generally indicates better performance for the same workload and test conditions.

### Q8. Why should the same benchmark command be used?

Using the same command helps keep the workload and test parameters consistent, making the results more comparable.

### Q9. Why is the number of virtual CPUs important?

The number of virtual CPUs affects the processing resources available to the virtual machine and can influence benchmark performance.

### Q10. Can one benchmark prove that a hypervisor is always faster?

No. Results depend on the workload, hardware, configuration, software versions, and test conditions. Repeated tests provide stronger evidence.

### Q11. Why are multiple runs useful?

Multiple runs help identify variations caused by background activity and other temporary system conditions. An average can provide a more reliable estimate.

### Q12. What are the limitations of this experiment?

The experiment focuses on one CPU workload, and results can be affected by VM configuration differences, host activity, and the limited number of benchmark runs.

## 13. References

1. Proxmox VE official documentation: https://pve.proxmox.com/pve-docs/
2. VMware Workstation documentation: https://docs.vmware.com/
3. sysbench project repository: https://github.com/akopytov/sysbench
4. Ubuntu documentation: https://help.ubuntu.com/