import os
import shutil

print('Current directory: ', os.getcwd())
presets = ['Documents', 'Rest']

# Creates directories based on user input and config
# for i in range(len(presets)):
#     filename = os.getcwd() + '/' + presets[i]
#     os.mkdir(filename)
# 
for folder, subfolders, filenames in os.walk(os.getcwd()):
    #print(os.path.basename(folder))
    if os.path.basename(folder) in presets:
        print("Outta here")
        continue
    for filename in filenames:
        if filename.endswith('.pdf'):
            #print(os.getcwd()+'/Documents/'+str(filename))
            shutil.move(filename, (os.getcwd() + '/Documents/' + filename))
        elif filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('jpeg'):
            shutil.move(filename, (os.getcwd() + '/Rest/' + filename))
