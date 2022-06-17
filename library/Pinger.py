from subprocess import call, run
import time, json


class Pinger:
    def __init__(self, hostname):
        self._host = hostname
        self._ping_counter = 0
        self._response = {}
        self._command = ['ping', '-c', '1', self._host]

    def ping(self):
        try:
            tic = time.perf_counter()
            result = (run(self._command, capture_output=True))
            toc = time.perf_counter()

            if result.returncode != 0:
                print(f"ping: Unreachable host: {self._host}")
                return -1

            self._ping_counter += 1

            self._response['host'] = self._host
            self._response['time'] = round((toc - tic) * 1000, 2)
            self._response['counter'] = self._ping_counter

            return json.dumps(self._response)

        except Exception as e:
            print(f"ping: {e}")
            return -1

