import time


class FPSCounter:
    """
    Calculates real-time Frames Per Second (FPS).
    """

    def __init__(self):
        self.previous_time = time.time()
        self.current_time = time.time()
        self.fps = 0

    def update(self):
        """
        Update FPS value.
        """

        self.current_time = time.time()

        elapsed = self.current_time - self.previous_time

        if elapsed > 0:
            self.fps = 1 / elapsed

        self.previous_time = self.current_time

        return int(self.fps)