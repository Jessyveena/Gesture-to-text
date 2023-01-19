import os
import string
# Create the directory structure
if not os.path.exists("dataset"):
    os.makedirs("dataset")
if not os.path.exists("dataset/train"):
    os.makedirs("dataset/train")
if not os.path.exists("dataset/test"):
    os.makedirs("dataset/test")
for i in range(0):  #for i in range(3):
    if not os.path.exists("dataset/train/" + str(i)):
        os.makedirs("dataset/train/"+str(i))
    if not os.path.exists("dataset/test/" + str(i)):
        os.makedirs("dataset/test/"+str(i))

for i in string.ascii_uppercase:
    if not os.path.exists("dataset/train/" + i):
        os.makedirs("dataset/train/"+i)
    if not os.path.exists("dataset/test/" + i):
        os.makedirs("dataset/test/"+i)
