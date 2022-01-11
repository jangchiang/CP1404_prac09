"""
Theeradon Somsri
CP1404 Practical09
Sort_files_2
"""
import os


def main():
    extension_category = {}  # category dictionary
    os.chdir('FilesToSort')
    for x in os.listdir('.'):  # x=FILENAME
        if os.path.isdir(x):
            continue

        extension = x.split('.')[-1]
        if extension not in extension_category:
            category = input("What category that want to sort {} files into? ".format(extension))
            extension_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(x, "{}/{}".format(extension_category[extension], x))


main()