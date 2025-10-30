import json
import matplotlib.pyplot as plt

with open("data/build_metrics.json") as f:
    data = json.load(f)

durations = [d["duration"] for d in data]
timestamps = [d["timestamp"] for d in data]

plt.figure(figsize=(8,4))
plt.plot(timestamps, durations, marker='o')
plt.title("Build Duration Trend")
plt.xlabel("Timestamp")
plt.ylabel("Duration (seconds)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
