import os
from random import randint
from datetime import datetime, timedelta


# Get today's date
today = datetime.now()

for i in range(1, 365):
    mydate = today - timedelta(days=i)
    # formated = mydate.isoformat()
    formated = mydate.strftime('%Y-%m-%dT%H:%M:%S')
    # formated = formated[:21]

    print(formated)

    for j in range(0, randint(0, 3)):
        d = str(i) + ' days and '+ str(j)+' commits'
        with open('file.txt', 'a') as file:
                file.write(d)
        os.system('git add .')
        os.system('git add .')        


# GIT_AUTHOR_DATE=2022-08-22T12:00:00 GIT_COMMITTER_DATE=2022-08-22T12:00:00