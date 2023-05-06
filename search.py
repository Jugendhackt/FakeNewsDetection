from googlesearch import search
from datetime import datetime, timedelta
import numpy as np

date = datetime.today() - timedelta(days=7)


date = 'after:'+np.array(str(date).split(' '))[0]

query = 'good'

query = query+' news '+str(date)


lst = []

for j in search(query, lang = 'en', stop=10):
    lst.append(j)

print(lst)

