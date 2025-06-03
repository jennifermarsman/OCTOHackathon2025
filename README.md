# OCTO Hackathon 2025
This is some sample code for use at a hackathon using the Azure OpenAI o3 model.  

## Setup
This project assumes that you are using our endpoint.  

Use the following commands in a python environment (such as an [Anaconda](https://www.anaconda.com/download) prompt window) to set up your environment.  This creates and activates an environment and installs the required packages.  For subsequent runs after the initial install, you will only need to activate the environment and then run the python script.  

### First run
```
conda create --name hackathon -y
conda activate hackathon

pip install -r requirements.txt
python responses.py
```

### Subsequent runs
```
conda activate hackathon
python responses.py
```