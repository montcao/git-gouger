import requests
#https://docs.github.com/en/rest/secret-scanning/secret-scanning?apiVersion=2022-11-28
def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/secret-scanning/alerts"
    resp = requests.get(url, headers=headers)
    body = resp.json()
    if "message" in body:
        note = body["message"]
    else:
        note = ""
    if resp.status_code == 200:
        secret_scanning = True
    else:
        secret_scanning = False

    return {
        "name": "Secret Scanning Enabled",
        "status": secret_scanning,
        "description": "GitHub scans for exposed secrets in commits to prevent accidental credential leaks",
        "notes": f"This will always fail if an administrator token is not used for authentication. If it still fails...you don't have secret scanning. {note}"
    }
