import json
import statistics
import sys
from pathlib import Path

METRICS_FILE = Path("data/build_metrics.json")

def load_metrics():
    if not METRICS_FILE.exists():
        return []
    with open(METRICS_FILE) as f:
        return json.load(f)

def detect_anomaly(new_duration, history):
    if len(history) < 3:
        return False

    durations = [h["duration"] for h in history]
    mean = statistics.mean(durations)
    stdev = statistics.stdev(durations)
    
    threshold = mean + 2 * stdev
    if new_duration > threshold:
        print(f"🚨 Anomaly detected! Build took {new_duration:.2f}s (threshold: {threshold:.2f}s)")
        return True
    return False

def main():
    history = load_metrics()
    with open("build_output.json") as f:
        latest = json.load(f)

    if detect_anomaly(latest["duration"], history):
        print("⚠️ Action Required: Investigate slow build")
        sys.exit(1)
    else:
        print("✅ Build within normal limits")

if __name__ == "__main__":
    main()
