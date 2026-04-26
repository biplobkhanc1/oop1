"""
with open ("biplob.text","w") as myfile:
    myfile.write("jkhjkh")
    print('my new file')
"""
"""
with open("biplob.text","r")as file:
    content=file.read()
    print(content)
    """
"""
import os
os.renames("biplob.text","biplob_khan")
"""
"""
import os
os.mkdir("2002")
os.mkdir("2002/aa")
with open ("name.png","w") as myfile:
    myfile.write("jkhjkh")
"""
"""
import shutil
shutil.make_archive("sumon","zip","sumon")
"""
"""
import csv
with open("biplob.csv",mode="w",newline=('')) as csvFile:
   csvFilewriter=csv.writer(csvFile)
    csvFilewriter.writerows(data)
"""
"""
import csv
with open("biplob.csv","r") as csvFile:
    csvFilereader=csv.reader(csvFile)
    for row in csvFilereader:
        print(row)
"""