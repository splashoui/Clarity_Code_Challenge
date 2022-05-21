
# Change this file location depend on your file directory

file_location = 'C:/Users/kurum/Desktop/Clarity_Code_Challenge/' 

class ParserHostConnection(object):
    
    """
    Uses the self.init_time, self.end_time, self.host_name
    inputs which has been taken from the user in MainProgram() class
    In order to:

    Parse the data with a time_init, time_end for all the connections to the host in the given period of time
    
    If there are connections in this given period of time to the host_name, it creates logs these connections 
    under "parsed_host_list_files" folder as a text file with the file name format : "init_time_end_time_host_name.txt"

    If there is not any connections happened in this given period of time to the host_name, it creates error logs 
    under "error_logs" folder as a text file with the file name format : "failed_init_time_end_time_host_name.txt"

    
    """

    def __init__(self, file_path, init_time, end_time, host_name):
        self.file_path = file_path
        self.init_time = init_time
        self.end_time = end_time
        self.host_name = host_name
 
    def create_list_of_hosts_to_connected(self):
        
        """

        Checks the generated connections to the given host name during the given time period. 
        Stores the connections in an empty list.

        """
        listed_information_to = []
        # Reads the input file line by line.  
        with open(self.file_path,'r') as f:
            text = f.read().splitlines()
            # Checks every line with for loop to find the match with given host_name and given period. 
            for i in range(len(text)):
                # If the connections are found, stores them in a list.
                if text[i].split(' ')[2:3] == [f'{self.host_name}'] and self.init_time <= int(text[i].split(' ')[0]) <= self.end_time:
                    listed_information_to.append(text[i])
        return listed_information_to,self.init_time,self.end_time,self.host_name

    def create_list_of_hosts_from_connected(self):

        """

        Checks the generated connections by the given host name during the given time period. 
        Stores the connections in an empty list.
    
        """

        listed_information_from = []
         # Reads the input file line by line.
        with open(self.file_path,'r') as f:
            text = f.read().splitlines()
            # Checks every line with for loop to find the match with given host_name and given period. 
            for i in range(len(text)):
                # If the connections are found, stores them in a list.
                if text[i].split(' ')[1:2] == [f'{self.host_name}'] and self.init_time <= int(text[i].split(' ')[0]) <= self.end_time:
                    listed_information_from.append(text[i])
        return listed_information_from
    
    def run_store_in_logs(self):

        """

        Calls the create_list_of_hosts_to_connected method to bring the listed information and store them in a log file.


        """
        # Takes the output of other function and assign to the new variables.
        listed_information_to,self.init_time,self.end_time,self.host_name = self.create_list_of_hosts_to_connected()
        
        # In case there are connections, print information and create log file with the file format "init_time_end_time_host_name.txt"
        if listed_information_to:
            print(f'{len(listed_information_to)} hosts were connected to the host "{self.host_name}" during the given period "{self.init_time}" and "{self.end_time}"\n{listed_information_to}')
            final_path = file_location +'logs/parsed_host_list_files'+'/'+str(self.init_time)+'_'+str(self.end_time)+'_'+self.host_name+'.txt'
            with open(final_path, 'w') as file:
                for row in listed_information_to:
                    s = "".join(map(str, row))
                    file.write(s+'\n')
            # Gives information about created log file and its name.
            print(f"Log file has been created under the {file_location +'logs/parsed_host_list_files'} folder with the name '{str(self.init_time)}_{str(self.end_time)}_{self.host_name}.txt'")

        # If there is no results, if the list is empty, It stores it under the folder error_logs
        # with the file format : failed_init_time_end_time_host_name.txt
        else:
            print(f'There is not any host connected to the host "{self.host_name}" yet during the given period "{self.init_time}" and "{self.end_time}"')
            final_path_error = file_location +'logs/error_logs'+'/'+'failed_'+str(self.init_time)+'_'+str(self.end_time)+'_'+self.host_name+'.txt'
            with open(final_path_error, 'w') as file:
                file.write(f'There is not any host connected to the host "{self.host_name}" yet during the given period "{self.init_time}" and "{self.end_time}"')
            print(f"Error log file has been created under the {file_location+'logs/error_logs'} folder with the name 'failed_{str(self.init_time)}_{str(self.end_time)}_{self.host_name}.txt'")

            