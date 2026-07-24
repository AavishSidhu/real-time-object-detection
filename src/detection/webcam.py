import cv2

from ultralytics import YOLO

from src.utils.fps import FPSCounter
from src.utils.object_counter import ObjectCounter


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

    fps_counter = FPSCounter()
    object_counter = ObjectCounter()

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

        fps = fps_counter.update()
        counts = object_counter.count(results, model)

        cv2.putText(
            annotated_frame,
            f"FPS: {fps}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        y_position = 80

        for object_name, count in counts.items():

            cv2.putText(
                annotated_frame,
                f"{object_name}: {count}",
                (20, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2,
                cv2.LINE_AA,
            )

            y_position += 30

        cv2.imshow(
            "YOLOv8 Real-Time Object Detection",
            annotated_frame,
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()