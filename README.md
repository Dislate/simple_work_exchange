# Basic implementation API for labor exchange on FastAPI
## How to run
### Runnig PostgreSQL
```
docker-compose -f docker-compose.dev.yaml up
```
### In next window terminal. Create venv for project in work directory
```
python3 -m venv venv
```
### Install all depends
```
pip3 install -r requirements.txt
```
### Run app 
```
python3 main.py
```

Open Swagger UI ```127.0.0.1:8000/docs``` in browser.