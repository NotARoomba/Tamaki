print("Starting")
# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP26, board.GP27, board.GP14,None, True, 2), # encoder #1 
    # reversed direction encoder with no button handling and divisor of 2
    (board.GP28, board.GP29, None, True, 2), # encoder #2
    )


encoder_handler.map = [ ((KC.UP, KC.DOWN, KC.MUTE),), # Standard
                        ((KC.VOLD, KC.VOLU, KC.MUTE),), # Extra
]

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros, encoder_handler)

# Define your pins here!
PINS = [board.GP0, board.GP1, board.GP2, board.GP4]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO(
    Press(KC.LCTL), # Copy
    Tap(KC.C),
    Release(KC.LCTL)
), KC.MACRO(
    Press(KC.LCTL), # Paste
    Tap(KC.V),
    Release(KC.LCTL)
), KC.MACRO(
    Press(KC.LCTL), # Undo
    Tap(KC.Z),
    Release(KC.LCTL)
), KC.MACRO(
    Press(KC.LCTL), # Redo
    Tap(KC.Y),
    Release(KC.LCTL)
)]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()