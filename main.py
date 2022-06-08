# Import of Libraries and Inherited classes
import datetime
from application.parser import ParserHostConnection
from application.unlimited_parser import UnlimitedParserHostConnection

# Defining the file path to read the input text file.
file_path = 'input_file/input-file-10000.txt'

class MainProgram(object):
    
    """
    
    Main page program, which inherits the attributes and methods of other two classes. 
    Provides 3 options to the user,
    
    0- Quit
    1- Normal Parser
    2- Unlimited Parser
    Based on the input of the user, it requests the related inputs from the user.
    
    1- Normal Parser 

    Parameters
        ----------
            init_time: : int
                initial time of the period
            end_time : int
                end time of the period
            host_name : str
                the name of the host
        ----------

    2- Unlimited Parser

    Takes only one input from the user which is host_name, since time period is defined, during the last hour.
    
    Parameters
        ----------
            host_name : str
                the name of the host
        ----------
    
    """

    def __init__(self):
        self.init_time = 1
        self.end_time = 1
        self.host_name = ''

    def user_inputs(self):
        option = int(input('Choose an operation: (1) Normal Parser or (2) Unlimited Parser\nPress (0) to quit.'))

        # Quit the program condition    
        if option == 0: 
            exit()

        # Normal parser to request inputs from the user.
        elif option == 1: 

            # .strip() being used in the case that user leaves space in the input
            init_time = input('Enter a 13 digits timestamp format initial time: ').strip()
            while not init_time or not init_time.isdigit():
                init_time = input('Incorrect init_datetime (Please try again): ')
                
            end_time = input('Enter a 13 digits timestamp format end time: ').strip()
            while not end_time or not end_time.isdigit():
                end_time = input(f'Incorrect end_datetime (Please try again): ')
                
            host_name = input('Enter a hostname (to see the list of connections to this host): ').strip()
            while not host_name or len(host_name) < 1 or host_name.isdigit():
                host_name = input('Incorrect hostname (Please try again): ')

            # Assigning the inputs to self. variable 
            # to be able to use these inputs inside the ParserHostConnection class and its methods
            
            # It capitalize the first letter and lower the rest of them.
            # Since our input host_names are first letter capital and rest lower,
            # To fix the user input in the case user inputs the host name all lower or all capital.
            host_name = host_name.capitalize()
            
            self.init_time = int(init_time)
            self.end_time = int(end_time)
            self.host_name = host_name
            
            inherit = ParserHostConnection(file_path, self.init_time, self.end_time, self.host_name)
            inherit.run_store_in_logs()
        
        # Unlimited parser to request the host name from the user.    
        if option == 2: 
            host_name = input('Enter a hostname: ')
            while not host_name or len(host_name) < 1 or host_name.isdigit():
                host_name = input('Incorrect hostname (Please try again): ').strip()
                
            # Assigning this input to self variable 
            #to be able to use host_name inside the UnlimitedParserHostConnection class and its methods.
            self.host_name = host_name
            
            inherit = UnlimitedParserHostConnection(file_path, self.host_name)
            inherit.last_one_hour_parse()

# The place where do I call the main program and start requesting user inputs
# Before getting to the ParserHostConnection or UnlimitedParserHostConnection classes.
if __name__ == '__main__':
    go_out = MainProgram()
    go_out.user_inputs()
