# ansible
My repo for ansible guides and demo material

## Pyenv
It's recommended that you use a virtual environment if running this locally or on a long lived system  
```bash
python3 -m venv .venv
source .venv/bin/activate
```


## Install ansible:
[Ansible Docs](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
```bash
python3 -m pip install -U setuptools
python3 -m pip install ansible
```

## Add Command Shell Completion with global configuration
[argcomplete docs](https://kislyuk.github.io/argcomplete/)  
```bash
python3 -m pip install argcomplete
activate-global-python-argcomplete
```

## Install Molecule and Docker driver plugin
[Molecule Docs]()
```bash
python3 -m pip install molecule
python3 -m pip install "molecule[docker]"
```

## Install Molecule plugins for TestInfra and Linting
[TestInfra Docs](https://testinfra.readthedocs.io/en/latest/)
[Ansible-Lint Docs](https://ansible-lint.readthedocs.io/en/latest/)
[Flake8 Docs](https://flake8.pycqa.org/en/latest/)
```bash
python3 -m pip install "molecule[lint]"
python3 -m pip install ansible-lint
python3 -m pip install flake8 testinfra
```
