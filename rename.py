import os

source = "C:/Users/jkvel/Downloads/source_Doc.pdf"

dest = "C:/Users/jkvel/Downloads/Destination_Watchdog/newName.pdf"

os.rename(source, dest)
print('File moved succesfully')