import time
from pylibftdi import BitBangDevice

# A
# Output
DTR = (1<<4)
RTS = (1<<2)
TX = (1<<0)
# Input
RX = (1 << 1)
CTS = (1 << 3)
DSR = (1 << 5)
DCD = (1 << 6)
# B
# Output
CLK = (1<<0)
DO = (1<<1)
CS = (1<<3)
TRST = (1<<4)
SRST = (1<<5)
# Input
DI = (1 << 2)

devA = BitBangDevice(interface_select=1)
devB = BitBangDevice(interface_select=2)

try:
    devA.direction = DTR | RTS | TX
    devA.port = 0
    devB.direction = CLK | DO | CS | TRST | SRST
    devB.port = 0

    time.sleep(1)

    # All inputs are default high by pull-up
    # All outputs are default low
    # If there is a short circuit between input and output the input is low 
    print("Check short circuit between input and output:")
    port_state_A = devA.port
    port_state_B = devB.port
    error = False
    if not (port_state_A & RX):
        print("RX is low but should be high")
        error = True
    if not (port_state_A & CTS):
        print("RX is low but should be high")
        error = True
    if not (port_state_A & DSR):
        print("RX is low but should be high")
        error = True
    if not (port_state_A & DCD):
        print("RX is low but should be high")
        error = True

    if not (port_state_B & DI):
        print("RX is low but should be high")
        error = True

    if not error:
        print("OK")

    # Chasing Lights
    # Every second another LED should be turned on
    # Always only one LED should be on at the same time
    print("")
    print("Check outputs:")

    time.sleep(2)

    print("CLK")
    devB.port = CLK
    time.sleep(1)

    print("DO")
    devB.port = DO
    time.sleep(1)

    print("CS")
    devB.port = CS
    time.sleep(1)

    print("TRST")
    devB.port = TRST
    time.sleep(1)

    print("SRST")
    devB.port = SRST
    time.sleep(1)
    devB.port = 0

    print("DTR")
    devA.port = DTR  
    time.sleep(1)

    print("RTS")
    devA.port = RTS
    time.sleep(1)

    print("TX")
    devA.port = TX
    time.sleep(1)
    devA.port = 0


    # For every button the corresponding Signal should be printed
    # It is possible to press multiple buttons. 
    # All corresponding signals should be printed in one line
    print("")
    print("Check inputs:")
    while True:
        port_state_A = devA.port
        port_state_B = devB.port

        string = ""

        if not (port_state_A & RX):
            string += "RX "
        if not (port_state_A & CTS):
            string += "CTS "
        if not (port_state_A & DSR):
            string += "DSR "
        if not (port_state_A & DCD):
            string += "DCD "

        if not (port_state_B & DI):
            string += "DI "
        
        print(" "*30, end="\r")
        print(string, end="")
        
        time.sleep(0.5)

finally:
    devA.close()
    devB.close()