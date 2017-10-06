import os
import shutil

def createDirs():
    print('Current directory: ', os.getcwd())
    presets = ['Documents', 'Rest', 'Images', 'Compressed', 'Programs', 'Music', 'Movies', 'Scripts']
    presets.sort()
    
    # Creates directories based on user input and config
    for i in range(len(presets)):
        filename = os.getcwd() + '/' + presets[i]
        os.mkdir(filename)
    
    return presets
    

def organize(presets):
    for folder, subfolders, filenames in os.walk(os.getcwd()):
        #print(os.path.basename(folder))
#        if os.path.basename(folder) in presets:
#            print("Outta here")
#            continue

        if os.path.basename(folder) != os.path.basename(os.getcwd()):
            continue

        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.docx') or filename.endswith('.doc') or filename.endswith('.epub') or filename.endswith('.tex'):
                shutil.move(filename, (os.getcwd() + '/Documents/' + filename))
            elif filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('jpeg'):
                shutil.move(filename, (os.getcwd() + '/Images/' + filename))
            elif filename.endswith('.mp3'):
                shutil.move(filename, (os.getcwd() + '/Music/' + filename))
            elif filename.endswith('.zip') or filename.endswith('.tar'):
                shutil.move(filename, (os.getcwd() + '/Compressed/' + filename))
            elif filename.endswith('.mp4') or filename.endswith('.mkv'):
                shutil.move(filename, (os.getcwd() + '/Movies/' + filename))
            elif filename.endswith('.deb'):
                shutil.move(filename, (os.getcwd() + '/Programs/' + filename))
            elif filename.endswith('.sh'):
                shutil.move(filename, (os.getcwd() + '/Scripts/' + filename))
            else:
                shutil.move(filename, (os.getcwd() + '/Rest/' + filename))

def main():
    organize(createDirs())

main()
