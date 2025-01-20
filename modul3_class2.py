"""
#create file
with open("Batch3.text","w") as MyFile: #file write
    MyFile.write("Hello world")

"""

"""
#Reading from a file

with open("Batch3.text","r") as MyFile: #file reading
    content= MyFile.read()
    print(content)

""" 

"""
#File rename

with open("module3.text","w") as MyFile: #file write/create
    MyFile.write("Hello Arafat")

import os
os.rename("module3.text","python3.text") #Rename "module3.text" file

"""

"""
#file Delete

with open("module3_Class2.text","w") as MyFile: #file write/create
    MyFile.write("Delete file")


import os
os.remove("module3_Class2.text")

"""

##........................................

"""
#Folder Creating
import os
os.mkdir('2024')
"""

"""
import os
os.mkdir('2024')
os.mkdir('2024/11')

with open('2024/11/Arafat.png',"w") as myfile:
    myfile.write("")   
"""

"""
#rename folder

import os

os.mkdir("2024/11")

#os.rename("2024/11","2024/nov")

"""

