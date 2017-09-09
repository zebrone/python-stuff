# import urllib2
# import unicodecsv as csv
# import os
# import sys
# import io
# import time
# import datetime
# import pandas as pd
# from bs4 import BeautifulSoup
# import sys
# import re

#def to_2d(l,n):
#    return [l[i:i+n] for i in range(0, len(l), n)]

with open('012.read.from.file.txt', 'r') as f:
    x = f.read()
# print(x[1])
req_text = x.split('\n')

print(req_text)

for phrase in req_text:
    print(phrase.strip())