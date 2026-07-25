import cv2

from ultralytics import YOLO


def process_video(
    model: YOLO,
    input_path: str,
    output_path: str,
    confidence: float = 0.5,
):
    """
    Run object detection on a video and save the output.
    """

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {input_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )

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

        if annotated_frame is not None:
            writer.write(annotated_frame)

    cap.release()
    writer.release()

    print(f"Saved output video to: {output_path}")