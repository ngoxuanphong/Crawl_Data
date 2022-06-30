from base import action
import os
Action = action.setup()
list_folder = os.listdir('C:/Users/KingSpec Store/Desktop/Phase_3_3')

list_file_name = []
for folder in list_folder:
    for file in os.listdir(f'C:/Users/KingSpec Store/Desktop/Phase_3_3/{folder}'):
        list_file_name.append(f'C:/Users/KingSpec Store/Desktop/Phase_3_3/{folder}/{file}')

print(len(list_file_name))
def dequydenchet(list_file_name):
    list_file_download = os.listdir('C:/Users/KingSpec Store/Downloads')

    list_file_dont_remove = []
    for file in list_file_name:
        # print(file[-14:-3] + 'xlsx')
        if file[-14:-3] + 'xlsx' not in list_file_download:
            # print(file)
            list_file_dont_remove.append(file)

    for file in list_file_dont_remove:
        # print(file)
        Action.get(file)
    if len(list_file_dont_remove) == 0:
        print('Done')
        return 'Done'
    else: 
        dequydenchet(list_file_name)
dequydenchet(list_file_name)