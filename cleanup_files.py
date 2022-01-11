"""
Theeradon Somsri
CP1404 Practical9
Cleanup_file
"""
import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for x in filenames:
            new_name = get_fixed_filename(x)
            print("Change name from {} to {}".format(x, new_name))
            full_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """this function will fix from the space change to _ and TXT to txt"""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")  # replace and fix the file type and name
    return new_name


if __name__ == '__main__':
    main()
