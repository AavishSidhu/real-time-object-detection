from pathlib import Path

from src.detection.model import load_model
from src.detection.predict import detect_image


IMAGE_PATH = Path("data/images/test.jpg")


model = load_model()

results = detect_image(
    model=model,
    image_path=IMAGE_PATH,
    confidence=0.50,
)

print("\nDetection Complete!\n")

for result in results:

    print(f"Image Size : {result.orig_shape}")

    print(f"Objects Detected : {len(result.boxes)}")

    print()

    for box in result.boxes:

        class_id = int(box.cls)

        confidence = float(box.conf)

        class_name = model.names[class_id]

        print(
            f"{class_name:<15}"
            f"{confidence:.2f}"
        )