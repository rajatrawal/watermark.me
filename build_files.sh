echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
chmod -R 777 /media
echo " BUILD END" 
