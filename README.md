# Virtual Mouse with Hand Tracking

A real-time hand gesture-based mouse controller using Python, OpenCV, and MediaPipe. This script lets you control your system cursor with your index finger and perform clicks by pinching your thumb and index finger together.

---

## Features

- Tracks a single hand and identifies key landmarks.
- Controls system cursor using index finger tip.
- Performs mouse clicks when thumb and index finger come close (pinch gesture).
- Frame skipping for smoother performance and less CPU load.

---

## Tech Stack

- **Python 3.8+**
- **OpenCV** (for image capture and processing)
- **MediaPipe** (for hand landmark detection)
- **PyAutoGUI** (to control mouse on screen)

---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shayan-sethi/gesturecursor.git
   cd hand-tracking-mouse
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyautogui
## Usage

Run the Python script:
```bash
python hand_tracking_mouse.py
