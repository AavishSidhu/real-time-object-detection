from src.detection.model import load_model
from src.detection.webcam import run_webcam


model = load_model()

run_webcam(
    model=model,
    confidence=0.5,
)