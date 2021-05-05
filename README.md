# Testing Python Thread Debugging in vscode

## Setup for Ubuntu

1. Install `code` and `code-insiders` via snap
2. Setup python virtual environments

```bash
git clone git@github.com:jonfen/vscode-python-debugging-tests.git
cd vscode-python-debugging-tests
./setup.sh
```

## Threading 

```bash
cd basic
code-insiders .
```

## Threading in a devcontainer

```bash
cd devcontainer 
code-insiders .
```

1. Install recommended extensions
2. Click on the green >< icon in the lower left hand corner.
3. Select `Reopen in Container` from the list

## Threading in flask

```bash
cd flask 
code-insiders .
```

## Threading in flask in a devcontainer

```bash
cd flask-devcontainer 
code-insiders .
```

1. Install recommended extensions
2. Click on the green >< icon in the lower left hand corner.
3. Select `Reopen in Container` from the list
4. Ctrl+Shift+˜ opens terminal in vscode and run these commands:
5. ```python3 -m pip install --upgrade pip```
6. ```python3 -m pip install -r ./requirements.txt```

TOOD: Add those commands to the Dockerfile

## Debugging

Press 'F5' to start the debugger

## Confusion

*Scenario:* There are two threads with hard coded breakpoints in each.

*Expectation:* When using the debugging navigation for a specific thread in the `CALL STACK` -- ONLY that thread breakpoint should progress

*Issue:* Stepping over a breakpoint on one thread also steps over the breakpoint on the other thread.

## References:
* https://github.com/microsoft/vscode-dev-containers/tree/master/containers/python-3/.devcontainer
* https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions
* https://flask.palletsprojects.com/en/master/debugging/#external-debuggers
* https://code.visualstudio.com/docs/python/tutorial-flask
* https://code.visualstudio.com/docs/python/debugging
* https://github.com/microsoft/containerregistry
* https://code.visualstudio.com/docs/remote/create-dev-container#_create-a-devcontainerjson-file
* https://snapcraft.io/install/code-insiders/ubuntu
* https://snapcraft.io/install/code/ubuntu
