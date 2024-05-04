from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

root.title("Number Plate Recognition")
root.geometry("500x500")  #fixed size of window
root.configure(background='#edecca')  #gives backgraound colour to page

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="D:\GitProjects\yolov4-custom-functions\data\images", title="Select a image", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    l1 = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image = img).pack()
    print(root.filename)
    print("python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images "+root.filename+" --plate")

b1 = Button(root, text= "Upload Image", command=open).pack()


text_label = Label(root, text="Text on the number plate: ", fg='Black', bg='#edecca')
text_label.pack()
text_label.config(font=('verdana', 18))   #font spec of label















# img = Image.open('kite.jpg')

# resized_img = img.resize((100,100))
# img = ImageTk.PhotoImage(resized_img)

# img_label = Label(root, image=img)
# img_label.pack(pady=(10,10))  #pack automatically places image in the window

# text_label = Label(root, text="FlipKart", fg='white', bg='#0096DC')
# text_label.pack()
# text_label.config(font=('verdana', 24))   #font spec of label


root.mainloop()