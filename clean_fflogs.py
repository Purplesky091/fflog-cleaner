import os
from datetime import datetime
import glob

# how many days old a file should be before it's deleted.
DELETION_AGE = 2 

def getFileDate(fileName):
    fileName = fileName.split(".")[0]
    parts = fileName.split("_")
    file_date = parts[len(parts) - 1]
    return datetime.strptime(file_date, "%Y%m%d")

# this string is the pattern that will retrieve act's fflog txt files.
# when plugged into glob.glob()
fflog_regex = os.path.join(os.getenv('APPDATA'), r'Advanced Combat Tracker\FFXIVLogs\*.log')
file_list = glob.glob(fflog_regex)

# this loop deletes anything that's 2 days or older
for file_name in file_list:
    file_date = getFileDate(file_name)
    todays_date = datetime.today()
    # how many days old the file is
    file_age = (todays_date - file_date).days 

    if file_age > DELETION_AGE:
        print(f'deleting file: {file_name}')
        os.remove(file_name)
    else:
        print(f'Keeping {file_name}')
