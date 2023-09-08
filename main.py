from docScan import *



"""
change value below to specify program path
1: walkthrough program
2: automate execution using paramters given at start
"""
path = 1


if __name__ == '__main__':
    print("")
    if path == 1:
        docScan_Walkthrough()
    elif path == 2:
        filename = f"enter filename (no format specifier): "
        filename = filename + ".png"
        img = easygui.fileopenbox()
        docScan_Auto(img, filename)

