# SDChat
implementation of a simple chat system

How to run:

1: clone repository:

    git clone https://github.com/mateusmagalhaes22/SDChat.git

2: enter project directory:

    cd SDChat

3: create a venv for the project:

    python -m venv ./

4: start the venv:

  on bash:

    source bin/activate

  on cmd:

    bin/activate.bat

  on PowerShell:

    bin/Activate.ps1

5: run database on docker:

    docker run --name sdchatdb -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mateusmagalhaes/sdchatdb:latest

6: install dependencies for back-end:

    pip install -r requirements.txt

7: run backend:

    flask --app api/aplication.py run

8: in other terminal, enter project directory and access front-end directory:

    cd SDChat/sdchat-front/

9: install dependencies for front-end:

    npm install

10: run front-end:

    npm run start
