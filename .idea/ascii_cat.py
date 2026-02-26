import os
cat_file = open('ascii_cat2.txt', 'r+')
cat = cat_file.read()
cat_file.close()

text = []
for i in range(len(cat)):
    text.append(cat[i])

ascii = []
for i in range(len(text)):
    ascii.append(str(ord(text[i])))