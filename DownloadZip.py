# importing necessary modules
import requests
from zipfile import ZipFile
from io import BytesIO
import zipfile
print('Downloading started')

#Defining the zip file URL
url = 'https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip'

# Split URL to get the file name
filename = url.split('/')[-1]

# Downloading the file by sending the request to the URL
req = requests.get(url)
print('Downloading Completed')

# extracting the zip file contents
#zipfile= zipfile.ZipFile(BytesIO(req.content))
#zipfile.extractall('C:/Downloads/NewFolder')

rz = requests.get(url)
with zipfile.ZipFile(BytesIO(req.content)) as z:
         z.extractall('C:/Downloads/NewFolder')