echo " BUILD START"
python3.9 -m pip install -r requirements.txt
chmod -R g+w  static/media/images/
chmod -R g+w  static/media/temp/
chmod -R g+w  static/media/output/
echo " BUILD END" 
