# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
import toml
																						
def main(conf):
    filename = filedialog.askopenfilename(initialdir = f'~',
										title = "Select a File",
										filetypes = (("XML files",
														"*.xml*"),
													("all files",
														"*.*")))
	
    exit
    return filename

    

if __name__ == "__main__":
	main()