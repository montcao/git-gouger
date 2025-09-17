import requests

def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
    resp = requests.get(url, headers=headers)
    body = resp.json()
    if "message" in body:
        note = body["message"]
    else:
        note = ""
    return {"name":"Found README.md",
            "status": resp.status_code == 200,
            "description" : "At a minimum, your repo should have a readme to let others (and future you) know what's going on.",
            "notes": note}
