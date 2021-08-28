
import json, requests, os, time
import pandas as pd

def get_match_by_id(id, step):
  m_id = str(id)
  request = requests.get('https://api.opendota.com/api/matches/' + m_id)
  if request.ok:
    data = request.json()
    print(id)
    file = open("../Data/Matches" + os.sep + m_id + '_data.json', 'w')
    json.dump(data, file)
    file.close

match_id = 3445646
  
for i in range(0,20000):
  get_match_by_id(match_id+i,i)
  time.sleep(2)