import cv2

from ultralytics import YOLO


def run_webcam(
    model: YOLO,
    confidence: float = 0.5,
):
    """
    Run real-time object detection using the webcam.
    """

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model.predict(
            source=frame,
            conf=confidence,
            verbose=False,
        )

        annotated_frame = results[0].plot()

        cv2.imshow(
            "YOLOv8 Real-Time Object Detection",
            annotated_frame,
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()