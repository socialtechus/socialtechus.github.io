import requests
import json

with open("payload.json") as file:
    test = json.load(file)
    
pr_url = test['pull_request']['url']
pr_content = json.loads(requests.get(pr_url).content)
status_url = pr_content['statuses_url']
latest_status = json.loads(requests.get(status_url).content)[0]
latest_status['target_url']

with open("target_url.txt", "w") as file:
    file.write(latest_status['target_url'])
