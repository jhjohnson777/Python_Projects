

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        #Creates a label giving the user instructions, placed using grid()
        self.text_lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.text_lbl.grid(row=0, column=0, padx=(20,10), pady=(20,10))

        #Text entry location placed using grid()
        self.text_ent = Entry(self.master, width=110)
        self.text_ent.grid(row=1, column=0, columnspan=3, padx=(20,10))

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        
        #Creates button to submit custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        #Places button using grid()
        self.custom_btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #New function called by Custom text button
    def customHTML(self):
        htmlText = self.text_ent.get() #User submitted text is retrieved from the entry location using get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
