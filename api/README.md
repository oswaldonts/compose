create a python env
apt install python3.10-venv
pip install virtualenv
python3 -m venv env

activate env
source env/bin/activate

install dependecies
pip install -r requirements.txt

start server
uvicorn main:app --reload

uvicorn main:app --host 0.0.0.0 --port 8000
