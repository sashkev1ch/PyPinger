from subprocess import call, run
import time, json


class Pinger:
    def __init__(self, hostname):
        self._host = hostname
        self._ping_counter = 0
        # response = {}
        self._command = ['ping', '-c', '1', self._host]

    def ping(self):
        try:
            tic = time.perf_counter()
            result = (run(self._command, capture_output=True))
            toc = time.perf_counter()

            if result.returncode != 0:
                print(f"ping: Unreachable host: {self._host}")
                response = {'host': self._host,
                            'time': -1,
                            'counter': self._ping_counter,
                            'reachable': False}
                return json.dumps(response)

            self._ping_counter += 1

            response = {'host': self._host,
                        'time': round((toc - tic) * 1000, 2),
                        'counter': self._ping_counter,
                        'reachable': True}
            return json.dumps(response)

        except Exception as e:
            print(f"ping: {e}")
            return -1

