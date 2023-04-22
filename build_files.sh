echo " BUILD START"
python3.9 -m pip install -r requirements.txt
chgrp -R www-data /var/task/media/
chmod -R g+w  /var/task/media/
echo " BUILD END" 
