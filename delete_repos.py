import os

import requests
from decouple import config

def delete_line(file_name, line_num):
    lines = open(file_name, 'r').readlines()
    try:
        while lines:
            lines.pop(line_num)
            open(file_name, 'w').writelines(lines)
    except IndexError:
        print('Line number {} does not exist in the file'.format(line_num))

def main():
   token = config('GITHUB_ACCESS_TOKEN')
   username = config('GITHUB_USERNAME')
   url = 'https://api.github.com/repos/{}'.format(username)
   print(url)
   headers = {'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token {} '.format(token)}

   lines = [line.strip() for line in open('repos.txt')]
   for repo in lines:
       print('Deleting repo: ' + repo)
       r = requests.delete(os.path.join(url, repo), headers=headers)
       if r.status_code == 204:
           print('{} deleted'.format(repo))
           delete_line('repos.txt', lines.index(repo))
       else:
           delete_line('repos.txt', lines.index(repo))
           print('{} not deleted'.format(repo))
        
if __name__ == '__main__':
    """
    This script will delete all the repos in the file 'repos.txt'
    It will also delete the line containing the repo name from the file
    Create a new file called 'repos_new.txt and populate it with the repos
    """
    main()