import board
import digitalio
import usb_hid
import time

# Minimal key codes
KC = {'N1': 0x1E, 'N2': 0x1F, 'N3': 0x20, 'N4': 0x21}
CC = {'BU': 0x6F, 'BD': 0x70, 'VU': 0xE9, 'VD': 0xEA}

# Setup HID
k = None
c = None
for d in usb_hid.devices:
    if d.usage_page == 0x01 and d.usage == 0x06:
        k = d
    elif d.usage_page == 0x0C and d.usage == 0x01:
        c = d

# Setup keys D6-D10
ks = []
for p in [board.D6, board.D7, board.D8, board.D9, board.D10]:
    pin = digitalio.DigitalInOut(p)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    ks.append({'p': pin, 's': pin.value})

# Setup encoders D0-D3 (digital pins)
e1a = digitalio.DigitalInOut(board.D0)
e1a.direction = digitalio.Direction.INPUT
e1a.pull = digitalio.Pull.UP

e1b = digitalio.DigitalInOut(board.D1)
e1b.direction = digitalio.Direction.INPUT
e1b.pull = digitalio.Pull.UP

e2a = digitalio.DigitalInOut(board.D2)
e2a.direction = digitalio.Direction.INPUT
e2a.pull = digitalio.Pull.UP

e2b = digitalio.DigitalInOut(board.D3)
e2b.direction = digitalio.Direction.INPUT
e2b.pull = digitalio.Pull.UP

# 2-step encoder state
e1s = (e1a.value, e1b.value)
e2s = (e2a.value, e2b.value)
e1t = 0  # Last trigger time
e2t = 0  # Last trigger time

# Minimal functions
def sk(kc):
    if k:
        r = bytearray(8)
        r[2] = kc
        k.send_report(r)
        time.sleep(0.05)
        k.send_report(bytearray(8))

def sc(cc):
    if c:
        c.send_report(bytearray([cc & 0xFF, cc >> 8]))

def get_2step_direction(old_state, new_state):
    # Only track A pin changes for 2-step detection
    if old_state[0] != new_state[0]:  # A pin changed
        if new_state[0]:  # A went high
            return 1 if old_state[1] else -1  # Check B state for direction
        else:  # A went low
            return -1 if old_state[1] else 1  # Check B state for direction
    return 0  # No change

# Macros
m = [KC['N1'], KC['N2'], KC['N3'], KC['N4'], KC['N1']]

print("Start!")

while True:
    # Scan keys
    for i, key in enumerate(ks):
        v = key['p'].value
        if v != key['s']:
            key['s'] = v
            if not v and i < len(m):
                sk(m[i])
    
    # Scan encoders with 2-step quadrature
    e1n = (e1a.value, e1b.value)
    e2n = (e2a.value, e2b.value)
    t = time.monotonic()
    
    # Encoder 1 with 2-step detection
    if e1n != e1s:
        if t - e1t > 0.05:  # 50ms debounce
            d1 = get_2step_direction(e1s, e1n)
            if d1 > 0:
                sc(CC['BD'])  # Clockwise = brightness down
            elif d1 < 0:
                sc(CC['BU'])  # Counter-clockwise = brightness up
            e1t = t
        e1s = e1n
    
    # Encoder 2 with 2-step detection
    if e2n != e2s:
        if t - e2t > 0.05:  # 50ms debounce
            d2 = get_2step_direction(e2s, e2n)
            if d2 > 0:
                sc(CC['VD'])  # Clockwise = volume down
            elif d2 < 0:
                sc(CC['VU'])  # Counter-clockwise = volume up
            e2t = t
        e2s = e2n
    
    time.sleep(0.01)