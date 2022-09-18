import json
import time
from subprocess import run
from library.decorators import timer_decorator


class Pinger:
    def __init__(self, hostname):
        self._host = hostname
        self._ping_counter = 0
        # response = {}
        self._command = ['ping', '-c', '1', self._host]

    @timer_decorator
    def make_ping(self):
        res = (run(self._command, capture_output=True))
        return res

    def ping(self):
        try:
            result = self.make_ping()
            if result['result'].returncode != 0:
                # print(f"ping: Unreachable host: {self._host}")
                response = {'host': self._host,
                            'time': -1,
                            'counter': self._ping_counter,
                            'reachable': False}
                return json.dumps(response)

            self._ping_counter += 1

            response = {'host': self._host,
                        'time': result['run_time'],
                        'counter': self._ping_counter,
                        'reachable': True}
            return json.dumps(response)

        except Exception as e:
            print(f"ping: {e}")
            return -1
