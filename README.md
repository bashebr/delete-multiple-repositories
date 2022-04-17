# Delete multiple repos

This is a simple script to delete multiple repositories from github. 

## Requirements
* Python3
* install `requests` as dependency
* Create a list of repos in a file, for example, `repos.txt` and populate it with the 
repos you want to delete
* You also need a github token and organization( or username)

## Usage
* Create a virtual env `virtualenv ven`
* Then run `pip install -r requirements.txt
* Run `python delete_repos.py` and enter the repo name
* That's it