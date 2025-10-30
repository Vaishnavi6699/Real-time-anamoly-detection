# Real-Time Anomaly Detection in CI/CD Pipelines

## 🎯 Goal
Detect abnormal build durations or failures using real-time data from CI/CD pipelines.

## ⚙️ Setup
1. Clone this repo.
2. Run locally:
   ```bash
   python app/main.py
   python scripts/anomaly_detector.py
   python scripts/update_metrics.py
   python scripts/visualize_metrics.py
   ```
3. Push to GitHub → check Actions tab.

## 🧠 How It Works
- Each build generates metrics (duration, success/failure).
- The anomaly detector checks if the new build deviates beyond mean + 2σ.
- If so, it flags an anomaly and fails the CI job.
- Metrics are updated automatically after each run.

## 📸 Screenshots

### 🧠 Build Execution
![Build Screenshot](https://github.com/Vaishnavi6699/Real-time-anamoly-detection/blob/main/build.jpg?raw=true)

### 📊 Metrics Visualization
![Metrics Visualization](https://github.com/Vaishnavi6699/Real-time-anamoly-detection/blob/main/metrics.jpg?raw=true)



