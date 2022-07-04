from subprocess import call, run
from library.Pinger import Pinger
import os, time, json

p = Pinger(hostname='8.8.8.8')

cnt = 1
all_time = 0


while True:
    resp = json.loads(p.ping())
    if resp['reachable']:
        all_time += resp['time']
        if resp['counter'] % 10 == 0:
            os.system('clear')
            print(f"avg_time: {round((all_time / resp['counter']), 2)} ms")
            time.sleep(1)
    else:
        os.system('clear')
        print(f"Unreachable!")
        time.sleep(3)
