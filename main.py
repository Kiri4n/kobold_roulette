import os
import tkinter.filedialog
import random
from time import sleep
from tkinter import *
import pygame
from PIL import ImageTk, Image

path_remove = ""
path_type = ""


def roulette():
    global path_remove, path_type
    roll_sound = pygame.mixer.Sound("Roll.mp3")
    roll_sound.play()
    sleep(2.25)
    if random.randint(0, 6) == 1:
        bt_roll.config(state=DISABLED)
        fail_sound = pygame.mixer.Sound("Fail.mp3")
        fail_sound.play()
        if path_type == "file":
            os.remove(path_remove)
        else:
            os.removedirs(path_remove)
        path_type = ""
        path_remove = ""
        label_path.config(text=path_remove)
    else:
        win_sound = pygame.mixer.Sound("Win.mp3")
        win_sound.play()


def chose_file():
    file_path = tkinter.filedialog.askopenfilename(
        title="selectionner  un fichier",
        initialdir='/',
    )
    if file_path:
        global path_remove, path_type
        path_type = "file"
        path_remove = file_path
        label_path.config(text=path_remove)
        bt_roll.config(state=NORMAL)


def chose_dir():
    dir_path = tkinter.filedialog.askdirectory(
        title="selectionner un dossier",
        initialdir='/',
    )
    if dir_path:
        global path_remove, path_type
        path_type = "dir"
        path_remove = dir_path
        label_path.config(text=path_remove)
        bt_roll.config(state=NORMAL)


if __name__ == '__main__':
    pygame.mixer.init()
    window_root = Tk()

    window_root.title('KOBOLD SUPREMACY')
    window_root.resizable(False, False)
    window_root.geometry('621x621')
    window_root.configure(bg="#F0EDE6")

    frame = Frame(window_root)
    frame.configure(bg="#F0EDE6")
    # image
    img = ImageTk.PhotoImage(Image.open("doit.png"))
    label_img = Label(frame, image=img, background="#F0EDE6")
    label_img.pack()
    # label instruction
    label_instruction = Label(
        frame,
        text='Choisisez le fichier ou le dossier à mettre dans la roulette ',
        font=('Ariale', 14)
    )
    label_instruction.pack()
    # label path
    label_path = Label(
        frame,
        text="",
        font=('Ariale', 9)
    )
    label_path.pack()

    # button file
    bt_file = Button(
        frame,
        text="selectionnez un fichier",
        command=chose_file
    )
    bt_file.pack(pady=5)

    # button dir
    bt_dir = Button(
        frame,
        text="selectionnez un dossier",
        command=chose_dir
    )
    bt_dir.pack(pady=5)

    # button roll
    bt_roll = Button(
        frame,
        text="Roll !",
        command=roulette,
        state=DISABLED
    )
    bt_roll.pack(pady=5)

    label_warning = Label(
        frame,
        text="ATTENTION ce logiciel supprimer VRAIMENT votre fichier/dossier",
        fg='red'
    )
    label_warning.pack(side=BOTTOM)

    frame.pack(expand=True)
    window_root.mainloop()
