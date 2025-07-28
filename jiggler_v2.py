import os
import sys
import pystray
import threading
import time
import pyautogui
from PIL import Image
from pynput import mouse, keyboard

# Po jakim czasie bezczynnosci jest ruszany kursor (w sekundach)
WAIT_TIME = 25

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

icon_path = resource_path("jigglerIcon.png")
icon_image = Image.open(icon_path)

def background_task():
    global last_activity
    while True:
        time.sleep(WAIT_TIME)
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 5, y)
        pyautogui.moveTo(x - 5, y)
        last_activity = time.time()

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

def setup_tray():
    icon = pystray.Icon("Jiggler", icon_image, "CursorJiggler", 
                        menu=pystray.Menu(

        pystray.MenuItem("Exit", after_click)))

    threading.Thread(target=background_task, daemon=True).start()

    icon.run()

if __name__ == "__main__":
    setup_tray()