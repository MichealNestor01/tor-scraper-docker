import os
from datetime import datetime

def createFileStructure():
    # get current date
    date = datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    # create necessary directories
    if not year in next(os.walk('/root/shared-area/'))[1]:
        os.mkdir(f"/root/shared-area/{year}")
        os.mkdir(f"/root/shared-area/{year}/{month}")
        os.mkdir(f"/root/shared-area/{year}/{month}/{day}")
    elif not month in next(os.walk(f'/root/shared-area/{year}'))[1]:
        os.mkdir(f"/root/shared-area/{year}/{month}")
        os.mkdir(f"/root/shared-area/{year}/{month}/{day}")
    elif not day in next(os.walk(f'/root/shared-area/{year}/{month}/'))[1]:
        os.mkdir(f"/root/shared-area/{year}/{month}/{day}")
    return f"/root/shared-area/{year}/{month}/{day}"

createFileStructure()