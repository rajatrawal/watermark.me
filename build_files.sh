echo " BUILD START"
python3.9 -m pip install -r requirements.txt
chgrp -R www-data /var/task/media/images/
chgrp -R www-data /var/task/media/images/
chmod -R g+w  /var/task/media/temp/
chmod -R g+w  /var/task/media/temp/
echo " BUILD END" 
