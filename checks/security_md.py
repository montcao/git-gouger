import requests
#https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository
def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    resp = requests.get(url, headers=headers)
    status = (resp.status_code == 200)
    body = resp.json()
    if "message" in body:
        note = body["message"]
    else:
        note = ""
    return {"name":"Found SECURITY.md",
            "status": status,
            "description" : "Defines how to report vulnerabilities responsibly",
            "notes": note}
