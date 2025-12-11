import argparse
from account_manager import AccountManager
from github_api import GitHubAPI
import random
import string

def generate_random_username(length=8):
    """
    Generates a random username.
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_password(length=12):
    """
    Generates a random password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def main():
    parser = argparse.ArgumentParser(description="GitHub Automation Tool")
    parser.add_argument("--repo_url", required=True, help="GitHub repository URL")
    parser.add_argument("--num_accounts", type=int, default=1, help="Number of fake accounts to create")
    parser.add_argument("--issue_title", required=True, help="Issue title")
    parser.add_argument("--issue_body", required=True, help="Issue body")
    parser.add_argument("--token", required=True, help="GitHub personal access token")

    args = parser.parse_args()

    repo_owner = args.repo_url.split('/')[3]
    repo_name = args.repo_url.split('/')[4].replace(".git", "")

    account_manager = AccountManager()
    github_api = GitHubAPI(args.token)

    # Create fake accounts
    for i in range(args.num_accounts):
        username = generate_random_username()
        password = generate_random_password()
        email = account_manager.get_temp_email()

        if email:
            account_manager.create_fake_account(username, password, email)  # Try creating account
            account_manager.register_account_on_github(username, password, email)  # Try registering on GitHub

    # Open issue and star repository
    github_api.open_issue(repo_owner, repo_name, args.issue_title, args.issue_body)
    github_api.star_repo(repo_owner, repo_name)

if __name__ == "__main__":
    main()
