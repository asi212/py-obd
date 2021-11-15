from src.obd.obd import OBD
import src.obd.commands as commands
import time


class StreamMetrics:
    """
    This class queries metrics at a specified interval

    metrics (List[str]): List of metrics names to be quieried
    refresh_rate (float/int): The time interval between queries
    verbose (bool): If True, prints the response to the screen
    """

    def __init__(self, connection=None, metrics=None, refresh_time=0.1, verbose=False):
        self.connection = connection
        self.metrics = metrics
        self.refresh_time = refresh_time
        self.verbose = verbose

    def run(self):
        t1 = time.time()
        while time.time() < t1 + 1:
            for i in range(len(self.metrics)):
                metric = commands[self.metrics[i]]
                response = self.connection.query(
                    metric
                )  # send the command, and parse the response
                if self.verbose == True:
                    print(response.value)
            time.sleep(self.refresh_time)
