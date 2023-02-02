# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "companyfacts.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as file:
    # printing all the contents of the zip file
    file.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    file.extractall(path=r"C:\Users\harshitha.r1\PycharmProjects\AWS_s3_RDS_final\temp")
    print('Done!')