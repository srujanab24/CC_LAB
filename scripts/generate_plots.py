"""Create benchmark charts from results/summary.json into images/.

  python scripts/generate_plots.py          # real charts from YOUR results
  python scripts/generate_plots.py --demo   # watermarked SAMPLE charts in images/demo/ (do NOT submit)
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DEMO = "--demo" in sys.argv
if DEMO:
    t1 = {"events_per_sec": 1000.0, "total_events": 10000, "lat_min_ms": 0.9, "lat_avg_ms": 1.0,
          "lat_p95_ms": 1.2, "lat_max_ms": 3.0}
    t2 = {"events_per_sec": 800.0, "total_events": 8000, "lat_min_ms": 1.1, "lat_avg_ms": 1.25,
          "lat_p95_ms": 1.6, "lat_max_ms": 4.5}
    out = Path("images/demo")
else:
    data = json.loads(Path("results/summary.json").read_text())
    t1, t2 = data["type1"], data["type2"]
    out = Path("images")
out.mkdir(parents=True, exist_ok=True)

names = ["Type-1\n(Proxmox VE)", "Type-2\n(VMware Workstation)"]
colors = ["#2a9d8f", "#e76f51"]


def mark(fig):
    if DEMO:
        fig.text(0.5, 0.5, "SAMPLE DATA - NOT REAL RESULTS", fontsize=26, color="gray",
                 alpha=0.35, ha="center", va="center", rotation=25)


def save(fig, name):
    mark(fig)
    fig.tight_layout()
    fig.savefig(out / name, dpi=150)
    plt.close(fig)


def bar(ax, key, title, ylabel, better):
    vals = [t1[key], t2[key]]
    ax.bar(names, vals, color=colors, width=0.55)
    ax.set_title(f"{title} ({better} is better)")
    ax.set_ylabel(ylabel)
    top = max(vals)
    ax.set_ylim(0, top * 1.15)
    for i, v in enumerate(vals):
        ax.text(i, v, f"{v:,.2f}", ha="center", va="bottom", fontweight="bold")


fig, ax = plt.subplots(figsize=(7, 5))
bar(ax, "events_per_sec", "CPU Throughput", "Events / second", "higher")
save(fig, "events_per_second_comparison.png")

fig, ax = plt.subplots(figsize=(7, 5))
bar(ax, "total_events", "Total Events in 10 s", "Events", "higher")
save(fig, "total_events_comparison.png")

lat = [("lat_min_ms", "Min"), ("lat_avg_ms", "Average"), ("lat_p95_ms", "95th percentile"), ("lat_max_ms", "Max")]
fig, ax = plt.subplots(figsize=(9, 5))
x = range(len(lat))
w = 0.38
b1 = ax.bar([i - w / 2 for i in x], [t1[k] for k, _ in lat], w, label="Type-1 (Proxmox VE)", color=colors[0])
b2 = ax.bar([i + w / 2 for i in x], [t2[k] for k, _ in lat], w, label="Type-2 (VMware Workstation)", color=colors[1])
ax.bar_label(b1, fmt="%.2f", padding=2, fontsize=8)
ax.bar_label(b2, fmt="%.2f", padding=2, fontsize=8)
ax.set_xticks(list(x))
ax.set_xticklabels([l for _, l in lat])
ax.set_ylabel("Latency (ms)")
ax.set_title("Latency Comparison (lower is better)")
ax.legend()
save(fig, "latency_comparison.png")

# Type-1 advantage in % (positive = Type-1 better)
delta_labels = ["Throughput", "Total events", "Min latency", "Avg latency", "P95 latency", "Max latency"]
deltas = [
    (t1["events_per_sec"] - t2["events_per_sec"]) / t2["events_per_sec"] * 100,
    (t1["total_events"] - t2["total_events"]) / t2["total_events"] * 100,
    (t2["lat_min_ms"] - t1["lat_min_ms"]) / t2["lat_min_ms"] * 100,
    (t2["lat_avg_ms"] - t1["lat_avg_ms"]) / t2["lat_avg_ms"] * 100,
    (t2["lat_p95_ms"] - t1["lat_p95_ms"]) / t2["lat_p95_ms"] * 100,
    (t2["lat_max_ms"] - t1["lat_max_ms"]) / t2["lat_max_ms"] * 100,
]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(delta_labels, deltas, color=["#2a9d8f" if d >= 0 else "#e76f51" for d in deltas])
ax.bar_label(bars, fmt="%+.2f%%", padding=3)
ax.axvline(0, color="black", lw=0.8)
ax.invert_yaxis()
ax.set_xlabel("Type-1 advantage over Type-2 (%)   [negative = Type-2 better]")
ax.set_title("Performance Delta: Type-1 vs Type-2")
save(fig, "performance_delta.png")

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
bar(axes[0][0], "events_per_sec", "Throughput", "Events / second", "higher")
bar(axes[0][1], "total_events", "Total events", "Events", "higher")
bar(axes[1][0], "lat_avg_ms", "Average latency", "ms", "lower")
bar(axes[1][1], "lat_p95_ms", "95th percentile latency", "ms", "lower")
fig.suptitle("Overall Performance Dashboard: Experiment 1", fontsize=15, fontweight="bold")
save(fig, "overall_performance_dashboard.png")
print(f"Charts saved to {out}/")
