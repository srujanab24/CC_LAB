"""Draw architecture + workflow diagrams (no benchmark data needed) into images/."""
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

Path("images").mkdir(exist_ok=True)

TYPE1 = [
    ("Physical Hardware\n(CPU with VT-x/AMD-V, RAM, Disk, NIC)", "#cfd8dc"),
    ("Proxmox VE Hypervisor\n(Linux kernel + KVM, runs on bare metal)", "#80cbc4"),
    ("Ubuntu Virtual Machine\n(2 vCPU, 2 GB RAM, 20 GB disk)", "#ffe082"),
    ("sysbench CPU benchmark\n(--cpu-max-prime=20000)", "#ffccbc"),
]
TYPE2 = [
    ("Physical PC Hardware\n(CPU with VT-x/AMD-V, RAM, Disk, NIC)", "#cfd8dc"),
    ("Host Operating System\n(Windows)", "#b0bec5"),
    ("VMware Workstation\n(Type-2 hypervisor, runs as an application)", "#ef9a9a"),
    ("Ubuntu Virtual Machine\n(2 vCPU, 2 GB RAM, 20 GB disk)", "#ffe082"),
    ("sysbench CPU benchmark\n(--cpu-max-prime=20000)", "#ffccbc"),
]


def stack(ax, layers, title):
    for i, (label, color) in enumerate(layers):
        ax.add_patch(FancyBboxPatch((0.05, i * 1.15 + 0.05), 3.9, 0.95,
                                    boxstyle="round,pad=0.02", fc=color, ec="#37474f", lw=1.2))
        ax.text(2, i * 1.15 + 0.52, label, ha="center", va="center", fontsize=10)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 5 * 1.15 + 0.1)
    ax.axis("off")


for layers, title, fname in [
    (TYPE1, "Type-1 Hypervisor (Bare-Metal): Proxmox VE", "architecture_type1.png"),
    (TYPE2, "Type-2 Hypervisor (Hosted): VMware Workstation", "architecture_type2.png"),
]:
    fig, ax = plt.subplots(figsize=(6.5, 6))
    stack(ax, layers, title)
    fig.tight_layout()
    fig.savefig(f"images/{fname}", dpi=150)
    plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
stack(axes[0], TYPE1, "Type-1: Proxmox VE (bare-metal)")
stack(axes[1], TYPE2, "Type-2: VMware Workstation (hosted)")
fig.suptitle("Hypervisor Architecture Comparison", fontsize=15, fontweight="bold")
fig.tight_layout()
fig.savefig("images/architecture_comparison.png", dpi=150)
plt.close(fig)

steps = [
    "Create Ubuntu VM on Proxmox VE (Type-1)",
    "Create Ubuntu VM on VMware Workstation (Type-2)",
    "Verify config: hostnamectl, lscpu, free -h, df -h",
    "Install sysbench",
    "Run sysbench cpu --cpu-max-prime=20000",
    "Save output and take screenshots",
    "Parse results and generate graphs",
    "Analyse and write conclusion",
]
fig, ax = plt.subplots(figsize=(15, 5))
ax.axis("off")
ax.set_xlim(0, 4)
ax.set_ylim(0, 2)
for i, s in enumerate(steps):
    row, col = divmod(i, 4)
    x, y = col + 0.06, 1 - row + 0.15
    ax.add_patch(FancyBboxPatch((x, y), 0.88, 0.7, boxstyle="round,pad=0.02", fc="#e3f2fd", ec="#1565c0", lw=1.3))
    ax.text(x + 0.44, y + 0.35, f"{i + 1}. " + "\n".join(textwrap.wrap(s, 24)),
            ha="center", va="center", fontsize=10)
    if col < 3:
        ax.annotate("", xy=(x + 1.0, y + 0.35), xytext=(x + 0.9, y + 0.35),
                    arrowprops=dict(arrowstyle="->", color="#1565c0", lw=1.6))
ax.set_title("Experiment Workflow", fontsize=15, fontweight="bold")
fig.tight_layout()
fig.savefig("images/experiment_workflow.png", dpi=150)
plt.close(fig)
print("Diagrams saved to images/")
