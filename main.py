import os
from typing import Any, Tuple
from git.remote import PushInfo, Remote
from github import Github
from github.NamedUser import NamedUser
from haikunator import Haikunator
from pathlib import Path
from dotenv import load_dotenv
from git import Repo


def env_vars():
    env_file_name = '.env'
    root_folder = Path(__file__).parent
    env_path = root_folder.joinpath(env_file_name)
    if not env_path.exists():
        raise f'Environment file "{env_file_name}" in project root folder do not exists'
    load_dotenv(env_path)


def repo_name(prefix: str = None) -> str:
    haikunator = Haikunator()
    hk_name = haikunator.haikunate(token_length=0)
    git_repo_name = f'{prefix}-{hk_name}' if prefix else hk_name
    return git_repo_name


def github_user() -> NamedUser:
    g = Github(os.environ['GITHUBPERSONALTOKEN'])
    user = g.get_user()
    return user


def github_create_repo(
    user: NamedUser,
    repo_name: str,
    repo_private: bool = True
) -> Any:
    res = user.create_repo(repo_name, private=repo_private)
    return res


def github_repo_ssh_url(
    user: NamedUser,
    repo_name: str
) -> str:
    repo_remote = [r for r in user.get_repos(repo_name) if r.name == repo_name][0]
    return repo_remote.ssh_url


def github_email_name(user) -> Tuple[str, str]:
    email = [e for e in user.get_emails() if e.primary][0].email
    name = user.name
    return (email, name)


def create_local_repo(
    root_folder: str,
    github_ssh_url: str,
    email: str,
    name: str
) -> Repo:
    repo = Repo.init(root_folder)
    repo.config_writer().set_value("user", "email", email).release()
    repo.config_writer().set_value("user", "name", name).release()
    # origin = repo.create_remote('origin', github_ssh_url)
    repo.create_remote('origin', github_ssh_url)
    return repo


def commit_and_push_root(
    repo: Repo
) -> PushInfo:
    repo.git.add('.')
    repo.index.commit('First commit')
    res = repo.remote().push(refspec='{}:{}'.format('main', 'origin/main'))
    return res



# def main():
env_vars()
gh_user = github_user()
rp_name = repo_name()
gr_rp_res = github_create_repo(
    user=gh_user,
    repo_name=rp_name,
    repo_private=False
)
gr_rp_res.ssh_url
user_info = github_email_name(user=gh_user)
local_repo = create_local_repo(
    root_folder=Path(__file__).parent,
    github_ssh_url=gr_rp_res.html_url,
    email=user_info[0],
    name=user_info[1]
)
res = commit_and_push_root(repo=local_repo)
assert res != None
    

# if __name__ == "__main__":
#     main()
