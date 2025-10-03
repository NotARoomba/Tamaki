import board
import digitalio
import usb_hid
import time

KC = {
    'N1': 0x1E,
    'N2': 0x1F,
    'N3': 0x20,
    'N4': 0x21,
    'N5': 0x22,
    'N6': 0x23
}

keyboard_device = None

for device in usb_hid.devices:
    if device.usage_page == 0x01 and device.usage == 0x06:
        keyboard_device = device

rows = []
for pin in [board.D7, board.D8]:
    row_pin = digitalio.DigitalInOut(pin)
    row_pin.direction = digitalio.Direction.INPUT
    row_pin.pull = digitalio.Pull.UP
    rows.append(row_pin)

cols = []
for pin in [board.D6, board.D10, board.D9]:
    col_pin = digitalio.DigitalInOut(pin)
    col_pin.direction = digitalio.Direction.OUTPUT
    col_pin.value = True
    cols.append(col_pin)

matrix_state = [[False, False, False], [False, False, False]]

def sk(k):
    if keyboard_device:
        r = bytearray(8)
        r[2] = k
        keyboard_device.send_report(r)
        time.sleep(0.05)
        keyboard_device.send_report(bytearray(8))

def scan_matrix():
    global matrix_state
    
    for col_idx, col in enumerate(cols):
        col.value = False
        time.sleep(0.001)
        
        for row_idx, row in enumerate(rows):
            current_state = not row.value
            
            if current_state != matrix_state[row_idx][col_idx]:
                matrix_state[row_idx][col_idx] = current_state
                
                if current_state:
                    key_num = row_idx * 3 + col_idx
                    switch_names = ['SW6','SW5','SW1','SW2','SW3','SW4']
                    switch_name = switch_names[key_num]
                    print(f"Button {key_num+1} ({switch_name}) pressed!")
                    
                    if key_num < len(m):
                        sk(m[key_num])
        
        col.value = True

m = [KC['N1'], KC['N2'], KC['N3'], KC['N4'], KC['N5'], KC['N6']]

print("Matrix keyboard started!")

while True:
    scan_matrix()
    time.sleep(0.01)