import random
import time
import json

def run_build():
    print("Starting build...")
    duration = random.uniform(2.0, 8.0)  # seconds
    success = random.choice([True, True, True, False])  # 75% success
    time.sleep(duration)
    print(f"Build {'SUCCEEDED' if success else 'FAILED'} in {duration:.2f} seconds")

    build_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration,
        "success": success
    }

    with open("build_output.json", "w") as f:
        json.dump(build_data, f, indent=4)

if __name__ == "__main__":
    run_build()
