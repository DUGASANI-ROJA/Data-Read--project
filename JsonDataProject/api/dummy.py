import json
file = open('json_data_file.json')
data = json.load(file)
# if data['ok']:
#     for element in data['members']:
#         print(element)
#         # print(len(element), end='\n\n')
#         # print(type(element))
#         print(element['activity_periods'])
#         print(len(element['activity_periods']))
#         # print(element['activity_periods'])


from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

print(datetime_object)


