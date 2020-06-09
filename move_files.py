import LogGenModule
import os, shutil

def move_file(srcpath,despath,srcfile):
    try: 
        destination = despath+srcfile
        source = srcpath+srcfile
        shutil.copyfile(source,destination) # copies the source file to the destination
        os.remove(source) # deletes the destination file
    except Exception as e:
        LogGenModule.Exception("Issue while mpving the files")
        LogGenModule.Exception(e)