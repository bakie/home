#Home
This is a django project which helps me with home stuff. For now it only helps me to decide what to eat in the week.

###Creation of the project
I use pipenv so it is easy to run the project on another computer. The steps I did to start the project.
* mkdir ~/playground/home
* cd ~/playground/home
* pipenv install django~=3.0
* pipenv shell
* djang-admin startproject home .

###Running the project
The project runs using docker. Make sure you have installed docker!

in the root of the project simply run ```docker-compose up -d``` and that is all.
