virtualenv --no-site-packages --distribute .env && source .env/bin/activate.bat && pip install -r requirements.txt
python3 main.py
.env/bin/deactivate.bat