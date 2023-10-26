# Playground

Playground project to use python

[![First Job](https://github.com/RedPanda9000/PythonPlayground/actions/workflows/Basic.yaml/badge.svg)](https://github.com/RedPanda9000/PythonPlayground/actions/workflows/Basic.yaml)

---
#### Python development

1. Create a local virtual env, 
This is to keep project specific dependencies away from the host machine python. 
For example if you have a http client on the host at version 10.0 however the project is required to be at 8.1, then you create the project virtual env install the depencies into the project virtual env and start the shell and use that. 

This keeps the host and the project python dependencies seperate

Steps

    1. Create the virtual env 
    <project root> python3 -m venv env

    2. Activate the virtual env
    source env/bin/activate

    3. Do some work like installing the project dependencies 
    
    pip install -r requirements.txt

    4. Exit the terminal 

    deactivate 
---
 