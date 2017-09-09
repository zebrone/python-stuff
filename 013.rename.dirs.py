import os
import sys

# parameters:  
#   013.rename.dirs.py [root_folder] [-n]
#   -n activates preview mode: no rename will actually occur
# Example:
# python 013.rename.dirs.py D:/Work/Attività/2017 -n


#print (sys.argv) 

preview_only = False

if len(sys.argv) > 2:
    preview_only = sys.argv[2] == '-n'
    if preview_only:
        print("Preview mode on")
    
if len(sys.argv) > 1:
    basedir = sys.argv[1]
    
    print ("Working on folder: " + basedir)
    
    for fn in os.listdir(basedir):
      if not os.path.isdir(os.path.join(basedir, fn)):
        continue # Not a directory
      if  '[' in fn and  ']' in fn:
        print(fn + ' is ok, no rename needed.') 
        continue # Already in the correct form
      if  '[' not in fn and  ']' not in fn:
        new_name = fn[:10].replace('_','-') + " [Aviva]" + fn[10:]
        print("  - Renaming {" + fn + '} to {' + new_name + '}') 
        if not preview_only:
            os.rename(os.path.join(basedir, fn),
                    os.path.join(basedir, new_name))
        continue # Invalid format
else:
    print ('Missing command line parameter (folder root, example: f:/test)')  