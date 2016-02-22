# -*- coding: utf-8 -*-
import re

with open('text.txt', 'r+') as file:
    full = u''
    file_read = file.read()
    for line in file_read:
        lineF = re.sub('\W', ' ', line).lower()
        full += lineF

    full = full.split(' ')

    obj = {}
    for o in full:
        if o != '':
            if o not in obj :
                obj[""+o+""] = 1
            elif obj[""+o+""] > 0:
                obj[""+o+""] = obj[""+o+""] + 1

    with open('newtext.txt', 'w') as file_write:
        for i, k in obj.items():
            file_write.write(i+' ')
            file_write.write(str(k))
            file_write.write('\n')
