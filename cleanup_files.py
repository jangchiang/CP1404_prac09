"""
Theeradon Somsri
CP1404 Practical9
Cleanup_file
"""
import os

def get_fixed_filename(filename):
    '''this function will fix from the space change to _ and TXT to txt'''
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")  # replace and fix the file type and name
    return new_name