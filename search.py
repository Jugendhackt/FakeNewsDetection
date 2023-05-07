from googlesearch import search
from datetime import datetime, timedelta
import numpy as np


def search_(text):
    date = datetime.today() - timedelta(days=7)
    date = 'after:'+np.array(str(date).split(' '))[0]
    query = text+' news-article '+str(date)
    lst = []
    for j in search(query, stop=10, lang = 'en'):
        lst.append(j)
    return(lst)

