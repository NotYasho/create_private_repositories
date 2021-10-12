import os
import sys
import time
import itertools
import threading
from selenium import webdriver
from colorama import Fore as fc
from subprocess import getoutput

if len(sys.argv) < 2:
    path = input(f"{fc.LIGHTBLUE_EX}Enter the path of the Folder: {fc.WHITE}\n")
    repo = input(f"{fc.LIGHTBLUE_EX}Enter the name of Repository: {fc.WHITE}\n")
    os.chdir(path)
else:
    repo = sys.argv[1]


# Gets the username and password from the Environment Variables
username = os.environ['Github-Username']
password = os.environ['Github-Password']

# To run Chrome in background
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# For the loading animation
def animate():
    for c in itertools.cycle(['⡿ Creating', '⣟ Creating', '⣯ Creating', '⣷ Creating',
                            '⣾ Creating', '⣽ Creating', '⣻ Creating', '⢿ Creating']):
        if done:
            break
        sys.stdout.write(f'\r{fc.LIGHTBLUE_EX}{c}')
        sys.stdout.flush()
        time.sleep(0.1)

try:

    done = False
    threading.Thread(target=animate).start()

    driver = webdriver.Chrome(options=options)
    driver.get("https://github.com/new")

    # Logging In

    Username = driver.find_element_by_id('login_field')
    Username.send_keys(username)
    Password = driver.find_element_by_id('password')
    Password.send_keys(password)
    Submit = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
    Submit.submit()

    # Creating The Repository

    Repo_Name = driver.find_element_by_xpath('//*[@id="repository_name"]')
    Repo_Name.send_keys(repo)
    Is_Private = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
    Is_Private.click()
    Create_Repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    Create_Repo.submit()
    Get_remote = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[6]/span')
    remote_url = Get_remote.text

    driver.close()

    # Pushes the Repository to Github

    commands = [
        'git init',
        f'git remote add origin {remote_url}',
        'git add -A',
        'git commit -m "Initial commit"',
        'git push -u origin master'
    ]

    for c in commands:
        getoutput(c)

        # This will prevent it to print any messages in the Console
        # If you want them, Change "getoutput(c)" to os.system(c)

    done = True

    print(f"\r✔️{fc.LIGHTGREEN_EX} Created A New Private Repository: {repo} {fc.WHITE}")

except Exception:

    print(f"{fc.LIGHTRED_EX} Whoops! Something Went Wrong {fc.WHITE}")
    exit()

