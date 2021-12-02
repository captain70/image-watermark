from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog, messagebox


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def open_file():
    base_img = filedialog.askopenfilename(initialdir='/', title="select a file",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))

    return base_img


def add_watermark(text):
    try:
        image = open_file()
        opened_image = Image.open(image)
        image_height, image_width = opened_image.size
        draw = ImageDraw.Draw(opened_image)

        # Font
        font_size = int(image_width/15)

        image_font = ImageFont.truetype('/Library/fonts/Arial.ttf', font_size)

        # Position
        x, y = int(image_width/2), int(image_height/2)

        # Add watermark
        draw.text((x, y), text, font=image_font, fill='#76760B', stroke_width=5, anchor='ms')
        watermark_entry.delete(0, END)
        # Show new image
        try:
            opened_image.show()
            image_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            opened_image.save(image_path)
        except ValueError:
            messagebox.showinfo("alert", "Please save file")
    except AttributeError:
        messagebox.showwarning("warning", "Please Upload Image")


base = Tk()
base.title("Watermark App")
base.config(padx=100, pady=30, bg=YELLOW)
base.minsize(width=300, height=300)

title_label = Label(base, text="Watermark App", fg=GREEN, bg=YELLOW, padx=20, pady=20, font=(FONT_NAME, 30))
title_label.pack(pady=10)

logo = Image.open('Tuscan-Spring-3.jpeg')
logo = logo.resize((150, 150))
logo_img = ImageTk.PhotoImage(logo)

logo_label = Label(image=logo_img)
logo_label.pack(pady=10)

watermark_label = Label(text="Watermark Text", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
watermark_label.pack(pady=10)

watermark_entry = Entry(base, width=15)
watermark_entry.pack(pady=10)

base_label = Label(text="Open Image", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
base_label.pack(pady=10)

open_btn = Button(text="Open file", height=2, width=10, font="Ariel", bg="#20bebe",
                      fg="gray", highlightthickness=0, command=lambda: add_watermark(watermark_entry.get()))
open_btn.pack(pady=10)

exit_button = Button(base, text='Exit', height=2, width=10, font="Ariel", bg="#20bebe",
                     fg="gray", highlightthickness=0, command=base.destroy)


exit_button.pack(pady=20)

base.grab_set()
base.mainloop()


