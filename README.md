This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

A Flask based API backend was added in the *api* directory.

Backend requires postgreSQL DB for CRUD operations. For this purpose docker-compose.yml file has been created.

Please follow the steps in given order to run application.

1) run ```docker-compose up``` in *api* directory
2) create virtual environment with python3 interpreter. Name virtual environment as venv. (If you want to give different name, you will need to change venv in package.json file.
3) activate venv.
4) run ```pip3 install -r requirements.txt``` in api directory.
5) run ```python3 preset_db.py``` to populate prerequisite data and tables in postgreSQL DB.
6) run ```yarn``` in root directory to install javascript dependencies.
7) run ```yarn start-api``` to start backend.
8) run ```yarn start``` to start frontend.
