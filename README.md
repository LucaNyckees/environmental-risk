# Environmental Risk Evaluation for Buildings in Switzerland

## People

- Tom Beucler : [GitHub profile](https://github.com/tbeucler)
- Luca Nyckees : [GitHub profile](https://github.com/lucanyckees)

## Context

This is part of a bigger project in collaboration with [ECCE](https://www.unil.ch/ecce/fr/home.html) at the University of Lausanne (UNIL), whose general workflow can be represented as follows.

![alt text](https://github.com/LucaNyckees/environmental-risk/blob/main/figures/workflows/ecce_workflow.png?raw=true)

## Description

This particular project is consists in the blue module in the workflow image above. As a first step, we aim at applying climate models in order to obtain a geographical grid of predictions for specific target variables (e.g. hail or wind). Then, we provide a local indicator of environmental risk based on this grid. 

## Virtual environment
Use the following command lines to create and use venv python package:
```
python3.11 -m venv venv
```
Then use the following to activate the environment:
```
source venv/bin/activate
```
You can now use pip to install any packages you need for the project and run python scripts, usually through a `requirements.txt`:
```
python -m pip install -r requirements.txt
```
When you are finished, you can stop the environment by running:
```
deactivate
```

## Basic structure
```
├── LICENSE
|
├── config files (.env, .ini, ...)
|
├── README.md
│
├── docs/               
│
├── requirements.txt  
|
├── __main__.py
│
├── src/                
|     ├── __init__.py
|     └── _version.py
|
└── tests/
```