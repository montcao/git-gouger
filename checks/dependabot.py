import requests
#https://docs.github.com/en/rest/dependabot/alerts?apiVersion=2022-11-28#list-dependabot-alerts-for-a-repository
# Can use the rest api or just check the contents of the .github file
def run(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/.github"
    resp = requests.get(url, headers=headers)
    status = False
    description = "Keeps dependencies updated automatically to patch known vulnerabilities"
    body = resp.json()
    if "message" in body:
        note = body["message"]
    else:
        note = ""
    if resp.status_code != 200:
        return  {
            "name": "Dependabot configured",
            "status": status,
            "description": description,
            "notes": note

        }
    files = [item["name"] for item in resp.json()]
    if "dependabot.yml" in files:
        status = True
    return  {
            "name": "Dependabot configured",
            "status": status,
            "description": description,
            "notes": note,
        }
