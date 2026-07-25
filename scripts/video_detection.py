from pathlib import Path

from src.detection.model import load_model
from src.detection.video import process_video


INPUT_VIDEO = Path("data/videos/traffic.mp4")
OUTPUT_VIDEO = Path("data/outputs/traffic_detected.mp4")

model = load_model()

process_video(
    model=model,
    input_path=str(INPUT_VIDEO),
    output_path=str(OUTPUT_VIDEO),
    confidence=0.5,
)