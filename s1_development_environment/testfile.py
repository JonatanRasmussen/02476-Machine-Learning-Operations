import sys #import
print(sys.executable) # Location of the Python.exe used to run this code

########################################
### HOW TO RESET VIRTUAL ENVIRONMENT ###
########################################

# Step 1: Select global interpreter in statusbar at the bottom of VS Code
# Step 2: Run the following commands in PowerShell (VS Code terminal)

# pip freeze > requirements.txt
# Remove-Item -Recurse -Force .venv

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# python -m venv .venv
# .\.venv\Scripts\Activate
# pip install -r requirements.txt

