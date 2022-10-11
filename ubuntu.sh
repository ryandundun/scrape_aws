#Shell commands.txt

#update
sudo apt-get update

#get pip
sudo apt-get install python3-pip

#clone repo, then cd into it
git clone https://github.com/ryandundun/scrape_aws.git
cd scrape_aws

#to install all requirements
pip3 install -r requirements.txt

#extra commmand for playwright
playwright install
python -m playwright install
python3 -m playwright install-deps

