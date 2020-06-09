import pysnow
import json
import LogGenModule

LogGenModule.info("=============================")


try:
        LogGenModule.info("*******Fetching the Instance Details*******")
        
        with open('./json_files/snow_login.json') as json_data:#collects the data from the input file
                data = json.load(json_data)
                instancename = data["Instance Details"][0]["instance"]
                username = data["Instance Details"][0]["user"]
                paswd = data["Instance Details"][0]["password"]


        LogGenModule.info("Logging into ServiceNow Client of instance.."+instancename)

        #Logs in to the ServiceNow instance 
        snow_client = pysnow.Client(instance=instancename, user=username, password=paswd)

except Exception as e:
        LogGenModule.error(e)



def update_ticket(ticket_number,status,comments):
    try:

        LogGenModule.info("Updating Ticket..."+str(ticket_number))
        LogGenModule.info("opening INCIDENT table of ServiceNow Client..")
        #opens the incident table
        snow_client = pysnow.Client(instance=instancename, user=username, password=paswd)
        tname = snow_client.resource(api_path='/table/incident')
        #collects the provided data for the updation of ticket
        update = {'state': status ,'work_notes': comments }
        LogGenModule.info("Updating ticket with the details provided ServiceNow Client..\n "+str(update))
        updated_value = tname.update(query={'number': ticket_number }, payload=update)#loads the ticket with provided data
        LogGenModule.info("Ticket "+str(updated_value['number'])+" Updated..")
        status = updated_value['state']
        return "done"
        LogGenModule.info("Updated Status of the ticket : "+str(status))
        
    except Exception as e:
        LogGenModule.error(e)
        return "not done"

def re_assignto_none(ticket_number):
    try:

        LogGenModule.info("Updating Ticket...")
        LogGenModule.info("opening INCIDENT table of ServiceNow Client..")
        #opens the incident table'
        tname = snow_client.resource(api_path='/table/incident')
        #collects the provided data for the updation of ticket

        update = {"assigned_to" : " "}
        LogGenModule.info("Updating ticket with the details provided ServiceNow Client..\n "+str(update))

        updated_value = tname.update(query={'number': ticket_number }, payload=update)#loads the ticket with provided data
        return "done"
        LogGenModule.info("Ticket "+str(updated_value['number'])+" Updated..")
        #assigned_to = updated_value['assigned_to']
        #print(assigned_to)
        
    except Exception as e:
        LogGenModule.error(e)
        return "not done"

def reassign_group(ticket_number,group,status,comments):
    try:
        LogGenModule.info("Updating Ticket...")
        LogGenModule.info("opening INCIDENT table of ServiceNow Client..")
        tname = snow_client.resource(api_path='/table/incident')
        update = {"assignment_group" : group,'state': status ,'work_notes': comments}
        
        updated_value = tname.update(query={'number': ticket_number}, payload=update)#loads the ticket with provided data
        return "done"
        LogGenModule.info("Updating ticket with the details provided ServiceNow Client..\n "+str(update))
    except Exception as e:
        
        LogGenModule.error(e)
        return "not done"