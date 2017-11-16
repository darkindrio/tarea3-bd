import csv
import os
from lightning import Lightning
import numpy as np
data = []
lgn = Lightning(ipython=True, host='http://public.lightning-viz.org')
total_categories = []
with open("/home/andres/Documentos/ejemplo_abb/test_out.csv", 'rb') as f:
    data = list(csv.reader(f))
    #data[0][0] = data[0][0].replace("\xef\xbb\xbf", ""); 
for idx in range(len(data) - 1):
    a = str(data[idx]).split('t[')
    rating = a[1].replace("]", "")
    rating = rating.replace(" ", "")
    rating = rating.replace("'", "")
    rating = rating.replace('"', "")
    
    num = rating.split(",")
    aux_list = []
    for number in num:
        aux_list.append(number)
    print aux_list
    a = np.array(aux_list, dtype=np.float32)
    total_categories.append(a)
    idx += 1
    
lgn.histogram(total_categories[1], 5, zoom=False)
