from tkinter import *
from pynput.keyboard import Listener, GlobalHotKeys
from threading import Thread

from app import Application

def on_activate_z():
  try:
    app.create_screen_canvas()
  except:
    app.exit_screenshot_mode()

def destroy():
  root.destroy()

def start_key_logger():
  hotkeys = {
    '<ctrl>+<alt>+z': on_activate_z,
    '<ctrl>+<alt>+d': app.destroyframes,
    '<ctrl>+<alt>+q': destroy
  }
  with GlobalHotKeys(hotkeys) as listener:
    listener.join()

root = Tk()
app = Application(root)

thread = Thread(target=start_key_logger, daemon=True)
thread.start()

print("App started")
root.mainloop()