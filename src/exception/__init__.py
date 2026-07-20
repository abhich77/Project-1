import sys
import logging

def error_message_detail(error:Exception,error_detail:sys)->str:
    """
    extracts detailed error information including file name,line number and error messages
    """

    # extrct traceback details
    _,_, exc_tb=error_detail.exc_info()

    # get the file name where exception happened
    file_name=exc_tb.tb_frame.f_code.co_filename

    # create a formatted error message string
    line_number=exc_tb.tb_lineno
    error_message=f"Error message in python script:[{file_name}] at line number [{line_number}]:{str(error)}"


    logging.error(error_message)

    return error_message


class MyException(Exception):
    """
    custom exception class for handling errors 
    """
    def __init__(self,error_message:str,error_detail: sys):
        """
        
        initialise the exception with a detailed error message
        """
        super().__init__(error_message)

        self.error_message=error_message_detail(error_message,error_detail)


def __str__(self)->str:
    """
    return string representation of error message. 
    """
    return self.error_message          


