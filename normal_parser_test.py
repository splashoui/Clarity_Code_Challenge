import unittest
from os import path
import os

from application.parser import ParserHostConnection


file_path = 'input_file/input-file-10000.txt'

class Test(unittest.TestCase):

    def test_output_normal_parser(self):

        """
        
        Test that expected output is the same with the result.

        For given time period and host name.
        
        """

        init_time, end_time, host_name  = 1565647260788, 1565712329620 , 'Elius'

        test = ParserHostConnection(file_path, init_time, end_time, host_name)
        result = test.create_list_of_hosts_to_connected()[0]

        result_expected = ['1565654296574 Huzaifa Elius', '1565663076542 Donterius Elius', '1565663252175 Quenisha Elius', '1565678511214 Jasenya Elius', 
        '1565682623782 Nayda Elius', '1565693215297 Jahvion Elius', '1565703564215 Salone Elius', '1565711610926 Kyjah Elius']

        # Test that first and second are equal. If the values do not compare equal, the test will fail.
        self.assertEqual(list(result), result_expected)


    def test_host_name_all_lower_letters(self):

        """
        
        Test that expected output is the same with the result.

        For given time period and host name.
        
        """

        init_time, end_time, host_name  = 1565647260788, 1565712329620 , 'elius'

        test = ParserHostConnection(file_path, init_time, end_time, host_name.capitalize())
        result = test.create_list_of_hosts_to_connected()[0]

        result_expected = ['1565654296574 Huzaifa Elius', '1565663076542 Donterius Elius', '1565663252175 Quenisha Elius', '1565678511214 Jasenya Elius', 
        '1565682623782 Nayda Elius', '1565693215297 Jahvion Elius', '1565703564215 Salone Elius', '1565711610926 Kyjah Elius']

        # Test that first and second are equal. If the values do not compare equal, the test will fail.
        self.assertEqual(list(result), result_expected)


    def test_host_name_all_capital_letters(self):

        """
        
        Test that expected output is the same with the result.

        For given time period and host name.
        
        """

        init_time, end_time, host_name  = 1565647260788, 1565712329620 , 'ELIUS'

        test = ParserHostConnection(file_path, init_time, end_time, host_name.capitalize())
        result = test.create_list_of_hosts_to_connected()[0]

        result_expected = ['1565654296574 Huzaifa Elius', '1565663076542 Donterius Elius', '1565663252175 Quenisha Elius', '1565678511214 Jasenya Elius', 
        '1565682623782 Nayda Elius', '1565693215297 Jahvion Elius', '1565703564215 Salone Elius', '1565711610926 Kyjah Elius']

        # Test that first and second are equal. If the values do not compare equal, the test will fail.
        self.assertEqual(list(result), result_expected)

    def test_log_file(self):

        """

        Test that if the log file has been created correctly with the correct name
        
        """

        init_time, end_time, host_name  = 1565647260788, 1565712329620 , 'Elius'

        test = ParserHostConnection(file_path, init_time, end_time, host_name)
        output = test.run_store_in_logs()
        # Test that if the log file log has been created correctly with correct name under the correct directory.

        folder_name = 'logs/parsed_host_list_files'
        final_name = folder_name+'/'+str(init_time)+'_'+str(end_time)+'_'+host_name+'.txt'
        result = path.exists(final_name)
        self.assertTrue(result)

    def test_error_log_file(self):

        """

        Test that if the error log file has been created with the correct name.

        In this case there is no connections found.

        For this goal, choosing a time period that there is no connections to that host_name
        
        """

        init_time, end_time, host_name  = 1565647228897, 1565647376373 , 'Lasheena'

        test = ParserHostConnection(file_path, init_time, end_time, host_name)
        output = test.run_store_in_logs()
        # Test that if the ERROR log file log has been created correctly with correct name under the correct directory.

        folder_name_error = 'logs/error_logs'
        final_path_error = folder_name_error+'/'+'failed_'+str(init_time)+'_'+str(end_time)+'_'+host_name+'.txt'
        result = path.exists(final_path_error)
        self.assertTrue(result)


    def test_information_stored(self):
        
        """

        To check if the information has been stored in the log file
        If the log file is empty or not.

        """

        init_time, end_time, host_name  = 1565647260788, 1565712329620 , 'Elius'

        test = ParserHostConnection(file_path, init_time, end_time, host_name)
        output = test.run_store_in_logs()

        folder_name = 'logs/parsed_host_list_files'
        final_name = folder_name+'/'+str(init_time)+'_'+str(end_time)+'_'+host_name+'.txt'
        
        # To check if the file is empty or stored with information
        file_size = os.stat(final_name).st_size != 0
        self.assertTrue(file_size)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
