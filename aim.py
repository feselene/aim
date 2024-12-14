import ctypes
import PIL.ImageGrab
import PIL.Image
import os
import mss
import threading
import time

S_HEIGHT, S_WIDTH = (PIL.ImageGrab.grab().size)
GRABZONE = 1

class FoundEnemy(Exception):
    pass

class triggerBot():
    def __init__(self):
        self.last_click_time = 0
        self.click_cooldown = 0.1  # Minimum time between clicks in seconds

    def click(self):
        current_time = time.time()
        ctypes.windll.user32.keybd_event(0x54, 0, 0, 0)  # Press T (0x54 is the virtual keycode for 'T')
        ctypes.windll.user32.keybd_event(0x54, 0, 2, 0)
        if current_time - self.last_click_time >= self.click_cooldown:
            ctypes.windll.user32.keybd_event(0x54, 0, 0, 0)  # Press T (0x54 is the virtual keycode for 'T')
            ctypes.windll.user32.keybd_event(0x54, 0, 2, 0)  # Release Ttttttttttttttttttttttttttttttttttttttttttttttttttt
            self.last_click_time = current_time

    def is_red(self, r, g ,b):
        return r > 240

    def grab(self):
        with mss.mss() as sct:
            bbox=(int(S_HEIGHT/2-GRABZONE), int(S_WIDTH/2-GRABZONE), int(S_HEIGHT/2+GRABZONE), int(S_WIDTH/2+GRABZONE))
            sct_img = sct.grab(bbox)
            return PIL.Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    def scan(self):
        while True:
            pmap = self.grab()
            try:
                for x in range(1):
                    for y in range(1):
                        r, g, b = pmap.getpixel((x, y))
                        if self.is_red(r, g, b):
                            raise FoundEnemy
            except FoundEnemy:
                self.click()
            time.sleep(0.01)  # Prevent busy-waiting

if __name__ == "__main__":
    bot = triggerBot()

    # Start scan in a separate thread
    threading.Thread(target=bot.scan, daemon=True).start()

    while True:
        time.sleep(1)
