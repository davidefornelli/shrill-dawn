# Project

GitHub - Deploy new repository

## System info

- Microsoft Windows [Version 10.0.19042.867]
- WSL2 - Ubuntu "20.04.1 LTS (Focal Fossa)"
- Python 3.7.9

## Expected result

Create local repo in sync with new GitHub repository

## Expected behavior

- Create .venv
- Create local git repo with python
- Create GitHub remote

![Recording](./recording.svg)

## Repro steps:

- Copy, open, update and rename dev.env to .env
- Exec `make it`

## Acceptance criteria

Project content uploaded to new GitHub repository

## Reference

- [Makefile](https://dev.to/yankee/streamline-projects-using-makefile-28fe)
- [GitHub personal token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- [Python venv](https://docs.python.org/3/library/venv.html)
- [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)
- [GitPython](https://gitpython.readthedocs.io/en/stable/index.html)
- [Bug Template](https://docs.microsoft.com/en-us/azure/devops/boards/backlogs/manage-bugs?view=azure-devops&tabs=new-web-form)
- [Asciinema](https://asciinema.org/docs/how-it-works)
- [Asciinema to SVG](https://github.com/marionebl/svg-term-cli)
