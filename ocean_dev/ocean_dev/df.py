import json

import pandas as pd
from data_cool import *
print(len(location_test))
print(len(skill_test))
df1 = pd.DataFrame(location_test)
df2 = pd.DataFrame(skill_test)
df3 = pd.DataFrame(title_test)
preference_df=pd.DataFrame(pref_test)
loc_skill = df1.join(df2.set_index('preferences_id'), on='preferences_id')
powersh = loc_skill.join(df3.set_index('preferences_id'), on='preferences_id')
# print(loc_skill.to_json(orient='records'))
# ok = json.loads((powersh.to_json(orient='records')))
# print(ok)
# print(len(ok))
# i = 0

df = powersh.join(preference_df.set_index('id'), on='preferences_id')
print(df.to_json(orient='records'))


# horizontal_stack = pd.concat([df1, df2], axis=0)
# print(horizontal_stack.to_json(orient='records'))

# dfs = [df1, df2, df3]
# dfs = [df.set_index('preferences_id') for df in dfs]
# dfs[0].join(dfs[1:])
# print(dfs)