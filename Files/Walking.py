import os, shutil

for folderName, subFolders, filenames in os.walk('C:\\'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
    
    for subFolder in subFolders:
        if 'fish' in subFolder:                 #if there was a file named fish, delite it
            os.rmdir(subFolder)
            print('rmdir on ' + subFolder)
    
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))   #make a copy of all python files and
                                                                                            #rename them to have the .backup ext