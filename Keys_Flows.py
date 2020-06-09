import json
import LogGenModule


def find_flow(ticket_summary):
    try:
        #print(ticket_summary)
        with open('../json_files/keys.json') as key_data:# reads the Keys and Flows data from json file
            key_to_flow = json.load(key_data)


        Summary = ticket_summary
        Matches =0
        Flow = "NF"
        Escalate_to = "Not Found"
        tower = "NF"
        suffix = "NF"
        Summary = Summary.lower()
        for Combs in key_to_flow['KeytoFlowCombination']:
            Matches = 0
            for key in Combs['KeyWords']:
                if key.lower() in Summary: 
                    Matches +=1
                #print(key+ " " +str(Matches))
            if Matches == len(Combs['KeyWords']):
                Flow = Combs['Flow']
                Escalate_to = Combs['EscalateTo']
                tower = Combs['Tower']
                suffix = Combs['suffix']
                key_data = [Flow,Escalate_to,tower,suffix]

                #print("Selected Flow for summarry : "+ Flow)
                break;
            
    
        
        key_data = [Flow,Escalate_to,tower,suffix]

        
        #print("Selected Flow for summarry : "+ key_data)
        return key_data
    
    except Exception as e:
        LogGenModule.Exception("Issue while fetching the Flow for the ticket")
        LogGenModule.Exception(e) 

#summary =input("enter summary")
#find_flow(summary)
#print("Flowname "+find_flow(summary)[0])