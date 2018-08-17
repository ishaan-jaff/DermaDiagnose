
# taken from stack overflow 
### https://stackoverflow.com/questions/21866537/what-could-cause-an-open-file-dialog-window-in-tkinter-python-to-be-really-#slow
# this was taken entirely from the link
import tkinter as tk
from tkinter import filedialog
def getPath( ):
    root = tk.Tk()
    root.withdraw()
    
    
    root.update()
    file_path = filedialog.askopenfilename()

    return (file_path)

