# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install postgres and the dependencies
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql

sudo apt install libpq-dev python3-dev 

# Install the dependencies from the requirements.txt file
pip install -r requirements.txt

# Install wkhtmltopdf package
# Check the name of your linux system
lsb_release -c
# replace the name in the below codes in place of focal
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb

sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb

# Test run the server for checking if any issues are present(inside the folder where manage.py file is present)
python3 manage.py runserver
