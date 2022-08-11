from cProfile import label
from logging import root
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import urllib.request
from PIL import Image
import imagehash
import hashlib

#setting main variables
root = tk.Tk()
root.title("Hexamda")
root.geometry('800x600')
#root.iconbitmap('icon.png')
#img=ImageTk.PhotoImage(file='ico.png')
#root.iconphoto(True, img)
root.minsize(800,600)
root.resizable(width=True,height=True)
root.config(bg='#121212') # making darkmode as default

#setting light mode
def Light() :
    root.config(bg='#00FFFF')
    lbl.config(bg='#00FFFF',fg='#000000')
    imgurl.config(bg='#00FFFF',fg='#000000')
    imgloc.config(bg='#00FFFF',fg='#000000')
    flloc.config(bg='#00FFFF',fg='#000000')
    md5.config(bg='#00FFFF',fg='#000000')
    sha.config(bg='#00FFFF',fg='#000000')
    credits.config(bg='#00FFFF',fg='#000000')

#setting dark mode
def Dark() :
    root.config(bg='#121212')
    lbl.config(bg='#121212',fg='#00FFFF')
    imgurl.config(bg='#121212',fg='#00FFFF')
    imgloc.config(bg='#121212',fg='#00FFFF')
    flloc.config(bg='#121212',fg='#00FFFF')
    md5.config(bg='#121212',fg='#00FFFF')
    sha.config(bg='#121212',fg='#00FFFF')
    credits.config(bg='#121212',fg='#00FFFF')
#image url hashing
def urlhash() :
    link=str(url.get())
    urllib.request.urlretrieve(link,'rng')
    var = imagehash.average_hash(Image.open('rng'))
    return messagebox.showinfo('Your Hashed Code is ',var)

def imghash() :
    imgloc=ien.get()
    var1 = imagehash.average_hash(Image.open(imgloc))
    return messagebox.showinfo('Your Hashed Code is ',var1)


def filehash():
    floc=fent.get()
    h = hashlib.sha256()
    with open(floc,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return messagebox.showinfo('Your Hashed Code is ',h.hexdigest())

def md5hash() :
    mhash=ment.get()
    var2 = hashlib.md5(str(mhash).encode('utf-8'))
    return messagebox.showinfo('your Hashed Code is :',var2.hexdigest())

def shahash() :
    shash=sent.get()
    var3 = hashlib.sha256(str(shash).encode('utf-8'))
    return messagebox.showinfo('your Hashed Code is :',var3.hexdigest())

#setting main label
lbl =  tk.Label(root,text="Hexamda The Hashing Tool",font='Helvetica 20 bold italic underline',bg='#121212',fg='#00FFFF')
lbl.place(relx=0.5, rely=0.05,anchor=CENTER)

#creating a menu options
menu = tk.Menu(root)

#making and adding all options while ending with menu name 
item = tk.Menu(menu,tearoff=False)
#item.add_command(label='Hash Image',command='hashimg')
#item.add_separator()
item.add_command(label='Exit',command=root.destroy)
menu.add_cascade(label='File', menu=item)

#menu two for color mode
item2 = tk.Menu(menu,tearoff=False)
item2.add_command(label='Light',command=Light)
item2.add_command(label='Dark',command=Dark)
menu.add_cascade(label='Theme', menu=item2)

#finishing it with a menu option
root.config(menu=menu)

#setting up image from website
imgurl = tk.Label(root,text="Enter Image URL :",font='Helvetica 16',bg='#121212',fg='#00FFFF')
imgurl.place(relx=0.25,rely=0.15,anchor=CENTER)
url=tk.Entry(root,width=50,)
url.place(relx=0.67,rely=0.15,anchor=CENTER)

button1=tk.Button(root,text='Hash',command=urlhash)
button1.place(relx=0.67,rely=0.20,anchor=CENTER)

#setting up using device image
imgloc = tk.Label(root,text="Enter Image Path:",font='Helvetica 16',bg='#121212',fg='#00FFFF')
imgloc.place(relx=0.25,rely=0.25,anchor=CENTER)
ien=tk.Entry(root,width=50,)
ien.place(relx=0.67,rely=0.25,anchor=CENTER)
iloc=ien.get()

button2=tk.Button(root,text='Hash',command=imghash)
button2.place(relx=0.67,rely=0.30,anchor=CENTER)

#file location
flloc = tk.Label(root,text="Enter File Path :",font='Helvetica 16',bg='#121212',fg='#00FFFF')
flloc.place(relx=0.25,rely=0.35,anchor=CENTER)
fent=tk.Entry(root,width=50,)
fent.place(relx=0.67,rely=0.35,anchor=CENTER)


button3=tk.Button(root,text='Hash',command=filehash)
button3.place(relx=0.67,rely=0.40,anchor=CENTER)

#md5 hash compare
md5 = tk.Label(root,text="MD5 Hashing :",font='Helvetica 16',bg='#121212',fg='#00FFFF')
md5.place(relx=0.25,rely=0.45,anchor=CENTER)
ment=tk.Entry(root,width=50,)
ment.place(relx=0.67,rely=0.45,anchor=CENTER)

button4=tk.Button(root,text='Hash',command=md5hash)
button4.place(relx=0.67,rely=0.50,anchor=CENTER)

#sha Compare
sha = tk.Label(root,text="SHA256 Hashing :",font='Helvetica 16',bg='#121212',fg='#00FFFF')
sha.place(relx=0.25,rely=0.55,anchor=CENTER)
sent=tk.Entry(root,width=50,)
sent.place(relx=0.67,rely=0.55,anchor=CENTER)

button5=tk.Button(root,text='Hash',command=shahash)
button5.place(relx=0.67,rely=0.60,anchor=CENTER)

credits=tk.Label(root,text='This is a Program Created to Simulate Basic Hashing\nBY : S . Praveen Kumar\n1CR21AD044\n@Kanoro.2003',font='Helvetica 15 bold italic underline',bg='#121212',fg='#00FFFF')
credits.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()