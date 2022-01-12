"""
Theeradon Somsri
CP1404 practical 09
Cleanup_filename
"""

import os


def main():
    """Fix inconsistent file naming."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for x in filenames:
            clean_file_name(x)
            old_name = os.path.join(directory_name, x)
            new_name = os.path.join(directory_name, clean_file_name(x))
            os.rename(old_name, new_name)
            if new_name != old_name:
                print("Renaming {} to {}.".format(old_name, new_name))


def clean_file_name(filename):
    """Return a correctly formatted filename."""
    new_name = ''
    for pos, character in enumerate(filename):
        if pos == 0:  # for position is that in range
            new_name += filename[pos].upper()
        elif filename[pos].isupper() and filename[pos-1].islower():  # if it does not follow the first condition
            new_name += " " + character
        else:
            new_name += character
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()