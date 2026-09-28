"""Parse results/type1.txt and results/type2.txt -> results/summary.json + markdown table."""
import json
import re
from pathlib import Path

FIELDS = {
    "total_time_s": r"total time:\s+([\d.]+)s",
    "total_events": r"total number of events:\s+(\d+)",
    "events_per_sec": r"events per second:\s+([\d.]+)",
    "lat_min_ms": r"min:\s+([\d.]+)",
    "lat_avg_ms": r"avg:\s+([\d.]+)",
    "lat_p95_ms": r"95th percentile:\s+([\d.]+)",
    "lat_max_ms": r"max:\s+([\d.]+)",
}


def parse(path):
    text = Path(path).read_text()
    out = {}
    for key, pattern in FIELDS.items():
        m = re.search(pattern, text)
        if not m:
            raise ValueError(f"Could not find '{key}' in {path}")
        out[key] = float(m.group(1))
    return out


if __name__ == "__main__":
    t1, t2 = parse("results/type1.txt"), parse("results/type2.txt")
    Path("results/summary.json").write_text(json.dumps({"type1": t1, "type2": t2}, indent=2))
    print("Saved results/summary.json")
    for k in FIELDS:
        print(f"{k:16s} type1={t1[k]:<10} type2={t2[k]:<10}")
