#import existing python modules
import logging
import datetime

# defines the structure of the logs
# format defines the structure of the log... structure would be time , type of log , message of the log
# datefmt defines the structure of the time stamp
# filename defines the file in which the log would be stored
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',datefmt='%a, %d-%b-%Y %H:%M:%S -', filename = datetime.datetime.now().strftime('../Logs/log_%d_%m_%Y.log'))


#creates information log in the log file and prints the information log in the terminal
def info(message):
    logging.info(message)


#creates Error log in the log file and prints the error log in the terminal
def error(message):
    logging.error(message)
    print("Error: {}".format(message))


#Creates the log in the specified log file along with the error message and the complete exception occured
def Exception(exceptn):
    logging.exception(exceptn)

