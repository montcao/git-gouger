# git-gouger

git-gouger is a tool that checks a Git repository for best practice and security configurations. 

It can be run with `python3 main.py {org} {repo} [token]`

## Starting point

Currently, git-gouger will gouge out the configurations of a repo to determine if [best](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-access-to-your-repository) [practices](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories) are being followed. The focus is on security configurations with plans to dive deeper into the information that can be pulled with git.

Currently git-gouger checks:

- Branch Protection is enabled
- Code Scanning is enabled
- Depandabot is enabled
- Readme.MD exists
- Secret Scanning is enabled
- Security.MD exists

The goal is meant to help any developer or security engineer understand 

TODO:

- Add in a contribution.md (and more documentation)
- Group check outputs
- Implement GraphQL option with auth
- Implement a safe option to inspect code within the repo (and extend tools like git-secrets etc)
- Add in additional checks to make the tool feature rich
- Extend to GitLab



