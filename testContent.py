from platform import win32_is_iot
import yaml
from Content import *
from itertools import islice

with open("wiki_codes.yml", 'r') as ymaldata:
        try: yamlfile = yaml.safe_load(ymaldata)
        except yaml.YAMLError as exception: print(exception)

wikis = yamlfile['wiki_codes']
ten_wikis = list(islice(wikis, 1))

# print(ten_wikis)

with open("page_to_date.yml", 'r') as ymaldata:
        try: yamlfile = yaml.safe_load(ymaldata)
        except yaml.YAMLError as exception: print(exception)

intervals = yamlfile['time_intervals']
periods   = yamlfile['time_periods']
filters   = yamlfile['filters']

# print(periods[1])

counter=0
for wiki in range(len(ten_wikis)):
    # print(ten_wikis[wiki])
    for p in periods:
        period=list(periods.keys())[list(periods.values()).index(periods[p])]
        #print(time_period)
        for f in filters:
            filter=list(filters.keys())[list(filters.values()).index(filters[f])]
            #print(filter)
            for i in intervals:
                interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                #print(interval)
                counter+=1
                print(f'** Iteration #{counter}: wiki={ten_wikis[wiki]}, t_period={period}, filter={filter}, t_interval={interval}')
                Content.pages_to_date(wiki_code=ten_wikis[wiki], time_period=period, filter=filter, time_interval=interval)


