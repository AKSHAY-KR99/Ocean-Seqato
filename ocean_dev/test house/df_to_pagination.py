from datetime import datetime

from data_cool import obj1
import pandas as pd

df = pd.DataFrame(obj1)
# print(df)
page_size = 4
page_num = 1
offset = page_size * (page_num - 1)
# print(df[offset:offset + page_size])
date_list = ["2022-10-28 12:16:25"]
exact_date = datetime.strptime(date_list[0], "%Y-%m-%d %H:%M:%S")
taz = str(exact_date).split(" ")
print(taz)
texa = taz[0] + 'T' + taz[1]
print(texa)