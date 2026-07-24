from collections import Counter


class ObjectCounter:
    """
    Counts detected objects in a frame.
    """

    def count(self, results, model):
        counts = Counter()

        for box in results[0].boxes:

            class_id = int(box.cls)

            class_name = model.names[class_id]

            counts[class_name] += 1

        return counts