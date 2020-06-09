import subprocess
import datetime
import LogGenModule
import os, shutil
import update_incident
import move_files
import os, fnmatch

path = '../Queue/processed_files/' # path in which input XML files are stored
listOfFiles = os.listdir(path) #reads all the files in the provided dir
pattern ='*.txt'
res = ""

try :
    for file in listOfFiles:
        if fnmatch.fnmatch(file,pattern): # matches the pattern
            with open((path+file),'r') as textfile:
                lines = textfile.read().splitlines() # fetches the data from the output text file
                result = lines[-1]
                Number = lines[0]
                notes = lines[-2]
                escalate = lines[1]
            textfile.close()
            #### Moves the source file from processed files depending on the keyword ###
            if (result == "failed"):
                print("result is failed need to escalate")
                move_files.move_file(path,'../Queue/executing_files/',file)
                
            if (result == "executed"):  
                res = update_incident.update_ticket(Number,"Closed",notes)
                print(res)
                if (res == "done"):
                    LogGenModule.info("Moving the source file.."+str(file))
                    move_files.move_file(path,'../Queue/closed/',file)

            if (result == "remove_assignee"):
                res = update_incident.re_assignto_none(Number)
                print(res)
                if (res == "done"):
                    LogGenModule.info("Moving the source file.."+str(file))
                    move_files.move_file(path,'../Queue/closed/',file)

            if (result == "reassign_group"):
                res = update_incident.reassign_group(Number,escalate,"Assigned",notes)
                print(res)
                if (res == "done"):
                    LogGenModule.info("Moving the source file.."+str(file))
                    move_files.move_file(path,'../Queue/closed/',file)
        
except Exception as e:
    LogGenModule.Exception("Issue while updating the ticket")
    LogGenModule.Exception(e)




