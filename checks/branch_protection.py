import requests


# Reference: https://docs.github.com/en/rest/branches/branch-protection#get-branch-protection

def run(owner, repo, headers, branch="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/protection"
    resp = requests.get(url, headers=headers)
    body = resp.json()
    if "message" in body:
        note = body["message"]
    else:
        note = ""
    return {
        "name": "Branch protection enabled", 
        "status": resp.status_code == 200,
        "description": "Branch protection ensures that critical branches can't be directly pushed to. This forces peer review, pull requests, etc, to reduce chances of insecure code reaching production.",
        "notes": note
        }
