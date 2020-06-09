import pysnow
import json
import LogGenModule



def re_assignto_none(tname,ticket_number):
    try:

        LogGenModule.info("Updating Ticket...")
        LogGenModule.info("opening INCIDENT table of ServiceNow Client..")
        #opens the incident table'
        #tname = snow_client.resource(api_path='/table/incident')
        #collects the provided data for the updation of ticket

        update = {"assigned_to" : " "}
        LogGenModule.info("Updating ticket with the details provided ServiceNow Client..\n "+str(update))

        updated_value = tname.update(query={'number': ticket_number }, payload=update)#loads the ticket with provided data

        LogGenModule.info("Ticket "+str(updated_value['number'])+"Updated..")
        #assigned_to = updated_value['assigned_to']
        #print(assigned_to)

    except Exception as e:
        LogGenModule.error(e)

def reassign_group(tname,ticket_number,group):
    try:
        LogGenModule.info("Updating Ticket...")
        LogGenModule.info("opening INCIDENT table of ServiceNow Client..")
        update = {"assignment_group" : group}
        LogGenModule.info("Updating ticket with the details provided ServiceNow Client..\n "+str(update))
        updated_value = tname.update(query={'number': ticket_number }, payload=update)#loads the ticket with provided data

    except Exception as e:
        LogGenModule.error(e)


#reassign_group(ticket_number,"Network")

#re_assignto_none(ticket_number)