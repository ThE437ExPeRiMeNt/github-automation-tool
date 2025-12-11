import requests
import json

class GitHubAPI:
    def __init__(self, token):
        self.token = token

    def open_issue(self, repo_owner, repo_name, title, body):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "title": title,
            "body": body
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            print("Issue created successfully.")
        else:
            print(f"Failed to create issue. Status code: {response.status_code}, Response: {response.text}")

    def star_repo(self, repo_owner, repo_name):
        url = f"https://api.github.com/user/starred/{repo_owner}/{repo_name}"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.put(url, headers=headers)
        if response.status_code == 204:
            print("Repository starred successfully.")
        else:
            print(f"Failed to star repository. Status code: {response.status_code}, Response: {response.text}")
