import pandas as pd
from data_cool import obj1, obj2, data_set, preferences, grade_preferences, location_preferences, role_preferences, skill_preferences, title_preferences, function_preferences

# df1 = pd.DataFrame(obj1)
# df2 = pd.DataFrame(obj2)
# df = df1.join(df2.set_index('candidate_id'), on='candidate_id')
# print(df.to_json(orient='records'))
# df = pd.merge(df1, df2, on="candidate_id")
# # print(df.to_json(orient='records'))
# print(len(data_set))
# df3 = pd.DataFrame(data_set)
# newed = df3.query('update_time < "2022-08-13" ')
# print(newed.to_json(orient='records'))


location = pd.DataFrame(location_preferences)
grade = pd.DataFrame(grade_preferences)
l_g = location.join(grade.set_index('preferences_id'), on='preferences_id')
role = pd.DataFrame(role_preferences)
l_g_r = l_g.join(role.set_index('preferences_id'), on='preferences_id')
skill = pd.DataFrame(skill_preferences)
l_g_r_s = l_g_r.join(skill.set_index('preferences_id'), on='preferences_id')
title = pd.DataFrame(title_preferences)
l_g_r_s_t = l_g_r_s.join(title.set_index('preferences_id'), on='preferences_id')
function = pd.DataFrame(function_preferences)
if not function.empty:
    l_g_r_s_t = l_g_r_s_t.join(function.set_index('preferences_id'), on='preferences_id')
# frame = location.join(grade.set_index('preferences_id'), role.set_index('preferences_id'),
#                       skill.set_index('preferences_id'), title.set_index('preferences_id'))
# print(l_g_r_s_t.to_json(orient='records'))
# a3 = a1.join(a2.set_index('preferences_id'), on='preferences_id')

# a4 = pd.DataFrame(preferences)
# print(a3.to_json(orient='records'))
# a5 = a4.merge(a3, left_on='id', right_on='preferences_id')
# print(a5.to_json(orient='records'))

prefe = pd.DataFrame(preferences)
final = prefe.join(l_g_r_s_t.set_index('preferences_id'), on='id')
# print(final.to_json(orient='records'))
