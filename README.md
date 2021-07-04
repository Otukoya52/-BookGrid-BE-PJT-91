# BookGrid-BE-PJT-91

### Steps to pull and run the project on your computer
- fork this repository
- create a folder for the project on your PC
- cd into the folder
- initialize a repository using **git init**
- add a remote link to your fork of the repository using **git remote add origin** ***link to your forked repo***
- add a remote link to the repository using **git remote add upstream https://github.com/zuri-training/BookGrid-BE-PJT-91**
- pull from the repository using **git pull origin main**
- cd into the **bookgrid_proj** you just pulled
- install django 3.1.7 using a virtual environment. In my case, **pipenv install django==3.1.7**
- install the requirements for the projects in the requirements.txt file using **pip install -r requirements.txt**
- gitignore the pipfile and pipfile.lock by adding them each on newlines in the git ignore file 
- make migrations using:
  - **python manage.py makemigrations**
  - **python manage.py migrate**
- start the server using **python manage.py runserver**

**NB:** It is encouraged you make a **git commit -m"your message here"** each time you make a change on your local repo instead of doing multiple things and waiting till you want to make a git push. For example, if you are writing tests for multiple APIs, make a **git commit -m"Test for withdrawal API"** instead of waiting till you're done writing tests for all the APIs.

### Steps to push and make a PR 
- push to your fork of the repository using **git push origin main**
- login to github and go to your fork of the repository 
- make a pull request from the main branch of your forked repository to the main branch of the repository 
- make your PR as desciptive as possible, explaining what you did

### FAQs
##### psycopg2 failed to install? 
- you have to install libpq-dev if you are using Ubuntu or any Linux distro using **sudo apt-get install libpq-dev**
#### git push origin main didn't work? 
- push using **git push origin master**
- then login to github and go to your fork of the repository 
- make a pull request from the master branch of your fork to the main branch of your fork of the repository 
