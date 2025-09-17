import requests

def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        print(data)
        #TODO Parse general information from this