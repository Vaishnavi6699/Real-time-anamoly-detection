import json
from pathlib import Path

METRICS_FILE = Path("data/build_metrics.json")

def main():
    with open("build_output.json") as f:
        new_record = json.load(f)

    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            history = json.load(f)
    else:
        history = []

    history.append(new_record)
    history = history[-10:]  # keep last 10 builds

    with open(METRICS_FILE, "w") as f:
        json.dump(history, f, indent=4)

    print("✅ Metrics updated.")

if __name__ == "__main__":
    main()
