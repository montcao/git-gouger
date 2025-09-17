import requests
"https://docs.github.com/rest/code-scanning/code-scanning#list-code-scanning-alerts-for-a-repository"
def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts"
    resp = requests.get(url, headers=headers)
    note = ""
    status = False
    if resp.status_code == 200:
        status = True
    else:
        body = resp.json()
        if "message" in body:
            note = body["message"]
    return {"name" : "Code scanning enabled",
            "status" : status,
            "description" : "Code scanning should be enabled on the repository to detect insecure coding patterns and vulnerabilities before release.",
            "notes" : note
            }

