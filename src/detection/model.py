from ultralytics import YOLO


def load_model(model_name: str = "yolov8n.pt"):
    """
    Load a YOLOv8 model.

    Parameters
    ----------
    model_name : str
        Name of the pretrained model.

    Returns
    -------
    YOLO
        Loaded YOLO model.
    """

    model = YOLO(model_name)

    return model