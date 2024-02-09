from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os   

root = Tk()
root.geometry("500x500")
root.title("Notepad-Untitled")
root.wm_iconbitmap("1.ico")

def change_font_style(style):
    TextArea.config(font=(style, TextArea.cget("height")))
    
def change_font_size(size):
    TextArea.config(font=(TextArea.cget("font")[0], size))

def undo():
    TextArea.event_generate("<<Undo>>")

def redo():
    TextArea.event_generate("<<Redo>>")

def count_words(event=None):
    # Get the text from the text widget
    text = TextArea.get("1.0", "end-1c")
    # Split the text into words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    # Update the word count label
    word_count_label.config(text=f"Word Count: {word_count}")

# Text Area 
TextArea=Text(root, undo=True)
file=None
TextArea.pack(fill=BOTH, expand=True)

# Create a label to display the word count
word_count_label = Label(root, text="Word Count: 0")
word_count_label.pack(side=LEFT)

# Bind the count_words function to text modifications
TextArea.bind("<KeyRelease>", count_words)


# Scroll Bar 
Scroll= Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(comma=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
def newfile():
    global file
    root.title("Untitled--Notepad")
    file=None
    TextArea.delete(1.0,END)
def openfile():
    global file
    file= askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"--Notepad")
        TextArea.delete(1.0, END )
        f=open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()
                     
def savefile():
    global file
    if file==None:
        file= asksaveasfilename (initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")] )
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"--Notepad")
            print("File Saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
    


        
def exitfile():
    root.quit()
def about():
    showinfo("Notepad", " it creates and edits plain text documents.")
def copyfile():
    TextArea.event_generate("<<Copy>>")
def pastefile():
    TextArea.event_generate("<<Paste>>")
def cutfile():
    TextArea.event_generate("<<Cut>>")
if __name__=='__main__':
        
    Main_Menu = Menu(root)
    # File Menu
    Menu1=Menu(Main_Menu, tearoff=0)
    Menu1.add_command(label="New", command= newfile)
    Menu1.add_command(label="Open", command=openfile)
    Menu1.add_command(label="Save", command= savefile)
    Menu1.add_separator()
    Menu1.add_command(label="Exit", command= exitfile)
    Main_Menu.add_cascade(label="File", menu=Menu1)
    # Edit Menu
    Menu2=Menu(Main_Menu, tearoff=0)
    Menu2.add_command(label="Copy (Ctrl+C)", command=copyfile)
    Menu2.add_command(label="Cut (Ctrl+X)", command=cutfile)
    Menu2.add_command(label="Paste (Ctrl+V)", command=pastefile)
    Menu2.add_command(label='Undo', command=undo)
    Menu2.add_command(label="Redo", command=redo)
    # Font Style Menu
    font_style_menu = Menu(Menu2, tearoff=0)
    font_style_menu.add_command(label="Arial", command=lambda: change_font_style("Arial"))
    font_style_menu.add_command(label="Times New Roman", command=lambda: change_font_style("Times New Roman"))
    font_style_menu.add_command(label="Comic Sans MS", command=lambda: change_font_style("Comic Sans MS"))
    Menu2.add_cascade(label="Font Style", menu=font_style_menu)
    
    # Font Size Menu
    font_size_menu = Menu(Menu2, tearoff=0)
    font_size_menu.add_command(label="8", command=lambda: change_font_size(8))
    font_size_menu.add_command(label="10", command=lambda: change_font_size(10))
    font_size_menu.add_command(label="20", command=lambda: change_font_size(20))
    font_size_menu.add_command(label="40", command=lambda: change_font_size(40))
    Menu2.add_cascade(label="Font Size", menu=font_size_menu)
    
    Main_Menu.add_cascade(label="Edit", menu=Menu2)
    # Help Menu 
    Menu3=Menu(Main_Menu, tearoff=0)
    Menu3.add_command(label='About Notepad', command=about)
    Main_Menu.add_cascade(label="Help", menu=Menu3)

    root.config(menu=Main_Menu)
    count_words()
    root.mainloop()

    