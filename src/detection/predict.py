from ultralytics import YOLO


def detect_image(
    model: YOLO,
    image_path: str,
    confidence: float = 0.25,
    save: bool = True,
):
    """
    Detect objects in an image.
    """

    results = model.predict(
        source=image_path,
        conf=confidence,
        save=save,
    )

    return results