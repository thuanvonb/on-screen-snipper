# Credit goes to Brett La Pierre's answer on Stack Overflow post
# https://stackoverflow.com/questions/49901928

from tkinter import *
import pyautogui
import os
import datetime
from PIL import ImageTk

miniimages = []

def take_bounded_screenshot(root, x1, y1, x2, y2):
  image = pyautogui.screenshot(region=(x1, y1, x2-x1+1, y2-y1+1))
  miniimages.append(MiniImage(root, image, (x1, y1)))
  
class Application():
  def __init__(self, master):
    self.snip_surface = None
    self.master = master
    self.start_x = None
    self.start_y = None
    self.current_x = None
    self.current_y = None
    self.win_frame_on = False
    self.screenshot_mode_on = False

    self.master.geometry('300x125+100+100')  # set new geometry
    self.master.title('On-screen Snipper')
    self.master.resizable(False, False)

    self.menu_frame = Frame(master)
    self.menu_frame.pack(expand=YES, padx=1, pady=1)

    self.buttonBar = Frame(self.menu_frame, bg="")
    self.buttonBar.pack()

    self.snipButton = Button(self.buttonBar, width=30, height=2, command=self.create_screen_canvas, text="Snip", bg="khaki1")
    self.snipButton.pack()

    self.destroyButton = Button(self.buttonBar, width=30, height=2, command=self.destroyframes, text="Destroy all", bg="firebrick1")
    self.destroyButton.pack()

    self.master_screen = Toplevel(self.master)
    self.master_screen.withdraw()
    self.master_screen.attributes("-transparent", "maroon3")
    self.picture_frame = Frame(self.master_screen, background="maroon3")
    self.picture_frame.pack(fill=BOTH, expand=YES)

    self.master.withdraw()

  def destroyframes(self):
    global miniimages
    for miniimage in miniimages:
      miniimage.frame.destroy()

    del miniimages
    miniimages = []

  def trigger_hide_screen(self):
    self.win_frame_on = not self.win_frame_on
    if self.win_frame_on:
      self.master.deiconify()
    else:
      self.master.withdraw()

  def enter_screenshot_mode(self):
    self.master_screen.deiconify()
    if self.win_frame_on:
      self.master.withdraw()

    for miniimage in miniimages:
      miniimage.frame.withdraw()
    self.screenshot_mode_on = True

  def create_screen_canvas(self):
    if self.screenshot_mode_on:
      return
    self.enter_screenshot_mode()

    self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="grey38")
    self.snip_surface.pack(fill=BOTH, expand=YES)

    self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
    self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
    self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

    self.master_screen.attributes('-fullscreen', True)
    self.master_screen.attributes('-alpha', .3)
    self.master_screen.lift()
    self.master_screen.attributes("-topmost", True)

  def on_button_release(self, event):
    self.master.update()
    take_bounded_screenshot(self.master, *map(int, self.real_coords))

    self.exit_screenshot_mode()
    return event

  def exit_screenshot_mode(self):
    self.snip_surface.destroy()
    self.master_screen.withdraw()
    if self.win_frame_on:
      self.master.deiconify()

    for miniimage in miniimages:
      miniimage.frame.deiconify()
    self.screenshot_mode_on = False

  def on_button_press(self, event):
    # save mouse drag start position
    self.start_x = self.snip_surface.canvasx(event.x)
    self.start_y = self.snip_surface.canvasy(event.y)
    self.snip_surface.create_rectangle(0, 0, 1, 1, outline='yellow', width=3, fill="maroon3")

  def on_snip_drag(self, event):
    self.current_x, self.current_y = (event.x, event.y)
    # expand rectangle as you drag the mouse
    self.snip_surface.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    self.real_coords = list(self.snip_surface.coords(1))


  def display_rectangle_position(self):
    print(self.start_x)
    print(self.start_y)
    print(self.current_x)
    print(self.current_y)


class MiniImage:
  def __init__(self, parent, image, coord):
    self.frame = Toplevel(parent)
    width, height = image.size
    x, y = coord
    self.frame.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    self.img = ImageTk.PhotoImage(image)
    self.label = Label(self.frame, image=self.img)
    self.label.place(x=-2, y=-2)
    self.prevX = None
    self.prevY = None
    self.frame.bind('<B1-Motion>', self.move)
    self.frame.bind('<ButtonPress-1>', self.click)
    self.frame.bind('<ButtonRelease-3>', self.destroy)
    self.frame.overrideredirect(True)
    self.frame.attributes("-topmost", True)

  def destroy(self, event):
    id = miniimages.index(self)
    del miniimages[id]
    self.frame.destroy()

  def click(self, event):
    self.prevX = event.x
    self.prevY = event.y

  def move(self, event):
    x, y = self.frame.winfo_pointerxy()
    self.frame.geometry(f"+{x - self.prevX}+{y - self.prevY}")


if __name__ == '__main__':
  root = Tk()
  app = Application(root)
  root.mainloop()