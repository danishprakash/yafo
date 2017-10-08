#! /usr/bin/python3

import os
import shutil
import argparse

'''
    Creates directories with a predefined set of extension-directory name dictionary, updates the dictionary if
    user provides custom rules as shown below.

    User defined rules:
        
        yafo --extensions .c .py .cpp --directory Programming

    will put all c, python and c++ files into the 'Programming' directory.
'''
def createDirs(ext, dirs):
    print('Current directory: ', os.getcwd())
    presets = {
            '.pdf':     'Documents',
            '.docx':    'Documents',
            '.epub':    'Documents',

            '.png':     'Images',
            '.jpeg':    'Images',

            '.mp3':     'Music',

            '.zip':     'Compressed',
            '.tar':     'Compressed',

            '.mp4':     'Movies',
            '.mkv':     'Movies',

            '.deb':     'Programs', }
            
    '''
        Check for user defined rules.
    '''
    if ext:
        for item in ext:
            presets[item] = ''.join(dirs)
    
    '''
        Creating directories with the presets dictionary.
    '''
    for i in (set(presets.values())):
        filename = os.getcwd() + '/' + i
        os.mkdir(filename)
    os.mkdir(os.getcwd() + '/Rest')
    
    return presets


'''
    this function does the moving part.
'''
def organize(presets):
    for folder, subfolders, filenames in os.walk(os.getcwd()):

        '''
            removes hidden directories.
        '''
        if subfolders:
            for i in range(len(subfolders)):
                if subfolders[i].startswith('.'):
                    del subfolders[i]
                    break

        '''
            Skips check for directories that are just being created or has been created
            i.e directories in the presets dictionary.
        '''
        if os.path.basename(folder) in presets.values() or os.path.basename(folder) == 'Rest':
            continue

        '''
            Moves the files with respect to their extension.
            The required directory is fetched using the extension of the file acting as the key to
            the presets dictionary.
            File extensions that are not mentioned anywhere are put into the 'Rest' directory.
        '''
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext in presets.keys():
                shutil.move(filename, (os.getcwd() + '/' + presets[ext] + '/' + filename))
            elif name != filename:
                shutil.move(filename, (os.getcwd() + '/Rest/' + filename))
    

'''
    parses the arguments if any and initiates the script.
'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extensions", dest="ext", nargs="*")
    parser.add_argument("-d", "--directory", dest="dirs", nargs="*")
    args = parser.parse_args()
    organize(createDirs(args.ext, args.dirs))
    

main()

