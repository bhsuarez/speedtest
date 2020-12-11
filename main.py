import speedtest
from pprint import pprint
import json
from datetime import datetime

print("Running speed test!")

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results_dict = s.results.dict()

results_dict_dump = json.dumps(results_dict)

dateTimeObj = datetime.now()

with open(f'speedtest-{dateTimeObj}.json','w') as json_file:

    json.dump(results_dict_dump, json_file)

pprint(results_dict_dump)
