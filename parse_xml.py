import xml.etree.ElementTree as ET
import re
import os, fnmatch
import os, shutil
import LogGenModule
import subprocess
import move_files


def run_script(suffix,Number,Flow,Configuration_Item,Escalation_Group,Summary,Tower,userID,location,Department): # executes the use case flow in the backend process
    try:
        path = '../Queue/InputFiles/'
        file = Number+'.xml'
        
        if suffix == 'NONE':
            cmd = 'start /b '+Flow+' '+Number+' '+"\""+Flow+"\""+' '+"\""+Configuration_Item+"\""+' '+"\""+Escalation_Group+"\""+' '+"\""+Summary+"\""+' '+"\""+userID+"\""+' '+"\""+location+"\""+' '+"\""+Department+"\""
        else:
            cmd = 'start /b '+suffix+' '+Flow+' '+Number+' '+"\""+Flow+"\""+' '+"\""+Configuration_Item+"\""+' '+"\""+Escalation_Group+"\""+' '+"\""+Summary+"\""+' '+"\""+userID+"\""+' '+"\""+location+"\""+' '+"\""+Department+"\""#+' >> D:\\custom_orch\\executing_files\\'+Number+'.txt' #command to choose the script flile
        #cmd = python ping.py asdfdf sdfdfs 10.181.11.121 fgfgfdgfg
        LogGenModule.info(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        LogGenModule.Exception("executing the usecase flow"+str(Flow))
        move_files.move_file(path,'../Queue/ProcessingFilesXML/',file)  # Moves the source file from processed files
    except Exception as e:
        LogGenModule.Exception("Issue while triggering the identified Flow")
        LogGenModule.Exception(e)

def exec_xml(ticket):
    try:

        path = '../Queue/InputFiles/' # path in which input XML files are stored
        listOfFiles = os.listdir(path) #reads all the files in the provided dir
        pattern ='*.xml'
        
        #print(len(fetch_data))
        dic = []



        try:
        
            for file in listOfFiles:
                if fnmatch.fnmatch(file,pattern): # matches the pattern 
                    #print(file)
                    tree = ET.parse(path+file) # parses the files in the given dir
                    root = tree.getroot()
                    if ticket == "Request" :
                        fetch_data = ['suffix','Task_Number','Flow','Escalation_Group','Task_Description','Tower','Requested_for','user_location','user_department']
                        for app in root.findall('Request'): #searches for the parent tag
                            for data in fetch_data: 
                                #print(data)
                                for l in app.findall(data): # searches for the mentioned child tag
                                    #print(l.text)            #gives the value of the child tag
                                    dic.append(l.text)
                        print(dic)

                        run_script(str(dic[0]),str(dic[1]),str(dic[2]),"NF",str(dic[3]),str(dic[4]),str(dic[5]),str(dic[6]),str(dic[7]),str(dic[8]))
                        del dic[:]

                    if ticket == "Incident" :
                        fetch_data = ['suffix','Number','Flow','Configuration_Item','Escalation_Group','Summary','Tower','User_ID','user_location','user_department']
                        for app in root.findall('Incident'): #searches for the parent tag
                            for data in fetch_data: 
                                #print(data)
                                for l in app.findall(data): # searches for the mentioned child tag
                                    #print(l.text)            #gives the value of the child tag
                                    dic.append(l.text)
                        print(dic)

                        run_script(str(dic[0]),str(dic[1]),str(dic[2]),str(dic[3]),str(dic[4]),str(dic[5]),str(dic[6]),str(dic[7]),str(dic[8]),str(dic[9]))
                        del dic[:]


        except Exception as e:
            LogGenModule.Exception("Issue while running the usecase XML file")
            LogGenModule.Exception(e)

    except Exception as e:
            LogGenModule.Exception("Issue while parsing the XML file")
            LogGenModule.Exception(e)
exec_xml("Request")