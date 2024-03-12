# For development use (simple logging, etc):

#if we are running on mini
sudo apt install lsb-release curl gpg



pip3 install -r requirements.txt
python3 main.py
# For production use:
# gunicorn app:app -w 1 --log-file -