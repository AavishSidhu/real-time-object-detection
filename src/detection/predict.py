from ultralytics import YOLO


def detect_image(
    model: YOLO,
    image_path: str,
    confidence: float = 0.25,
):
    """
    Detect objects in an image.
    """

    results = model.predict(
        source=image_path,
        conf=confidence,
        verbose=False,
    )

    annotated_image = results[0].plot()

    return annotated_image, results