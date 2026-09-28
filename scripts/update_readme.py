"""Fill the results table + auto summary in README.md from results/summary.json."""
import json
import re
from pathlib import Path

d = json.loads(Path("results/summary.json").read_text())
t1, t2 = d["type1"], d["type2"]


def pct(a, b):
    return (a - b) / b * 100


rows = [
    ("Total execution time (s)", "total_time_s", None),
    ("Total events processed", "total_events", "higher"),
    ("Events per second", "events_per_sec", "higher"),
    ("Minimum latency (ms)", "lat_min_ms", "lower"),
    ("Average latency (ms)", "lat_avg_ms", "lower"),
    ("95th percentile latency (ms)", "lat_p95_ms", "lower"),
    ("Maximum latency (ms)", "lat_max_ms", "lower"),
]
lines = ["| Metric | Type-1 (Proxmox VE) | Type-2 (VMware Workstation) | Difference (T1 vs T2) | Better |",
         "|---|---|---|---|---|"]
for label, key, better in rows:
    a, b = t1[key], t2[key]
    diff = f"{pct(a, b):+.2f}%"
    if better is None:
        win = "-"
    elif a == b:
        win = "Tie"
    else:
        win = "Type-1" if ((a > b) == (better == "higher")) else "Type-2"
    lines.append(f"| {label} | {a:g} | {b:g} | {diff} | {win} |")

eps = pct(t1["events_per_sec"], t2["events_per_sec"])
lat = pct(t1["lat_avg_ms"], t2["lat_avg_ms"])
faster = "Type-1 (Proxmox VE)" if eps > 0 else "Type-2 (VMware Workstation)"
summary = (f"\n**Auto-generated summary:** {faster} processed {abs(eps):.2f}% "
           f"{'more' if eps > 0 else 'fewer'} events per second in this run "
           f"({t1['events_per_sec']:g} vs {t2['events_per_sec']:g}), and Type-1's average latency was "
           f"{abs(lat):.2f}% {'lower' if lat < 0 else 'higher'} than Type-2's.\n")

block = "<!-- RESULTS_START -->\n" + "\n".join(lines) + "\n" + summary + "<!-- RESULTS_END -->"
p = Path("README.md")
text = p.read_text()
new = re.sub(r"<!-- RESULTS_START -->.*?<!-- RESULTS_END -->", lambda m: block, text, flags=re.S)
p.write_text(new)
print("README.md results table updated.")
