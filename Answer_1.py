import PIL.Image

from tkinter import filedialog
from tkinter import Tk
def main():

    Tk().withdraw()
    fname = filedialog.askopenfilename(filetypes=(("Image Files", "*.jpg"), ("All files", "*")))
    print(fname)

    img1 = PIL.Image.open(fname)


    fname = filedialog.askopenfilename(filetypes=(("Image Files", "*.png"),("Image Files", "*.jpg"), ("All files", "*")))
    print(fname)
    img2 = PIL.Image.open(fname)
    img21=img2.resize((200,200))


    img1.paste(img21, (500, 0))
    fname = filedialog.askopenfilename(filetypes=(("Image Files", "*.png"),("Image Files", "*.jpg") ,("All files", "*")))
    print(fname)
    img3 = PIL.Image.open(fname)
    img31 = img3.resize((200, 200))


    img1.paste(img31, (500, 500))
    fname = filedialog.askopenfilename(filetypes=(("Image Files", "*.png"),("Image Files", "*.jpg"), ("All files", "*")))
    print(fname)
    img4 = PIL.Image.open(fname)
    img41 = img4.resize((200, 200))


    img1.paste(img41, (0, 500))


    img1.show()
main()