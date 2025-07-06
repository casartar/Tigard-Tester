import time
from pylibftdi.device import Device
from pylibftdi.driver import FtdiError

# Number of GPIO pins (depending on the FTDI chip, this might vary)
NUM_GPIO_PINS = 8  # Common for FTDI2232H with 8 GPIO pins per port

def toggle_gpio_pins():
    try:
        with Device(device_id=None, interface_select=2) as dev_b:  # Port B (interface 2)
            dev_b.baudrate = 9600
            dev_b.ftdi_fn.ftdi_set_bitmode(0x3B, 0x01)  # Set all pins as output
            dev_b.write(bytes([0x00]))

        with Device(device_id=None, interface_select=1) as dev_a:  # Port A (interface 1)
            dev_a.baudrate = 9600
            dev_a.ftdi_fn.ftdi_set_bitmode(0x15, 0x01)  # Set all pins as output
            dev_a.write(bytes([0x00]))

        time.sleep(3)

        # Toggle GPIO pins on Port B
        with Device(device_id=None, interface_select=2) as dev_b:  # Port B (interface 2)
            dev_b.baudrate = 9600
            dev_b.ftdi_fn.ftdi_set_bitmode(0x3B, 0x01)  # Set all pins as output
            
            dev_b.write(bytes([1<<0]))
            time.sleep(1)
            dev_b.write(bytes([1<<1]))
            time.sleep(1)
            dev_b.write(bytes([1<<3]))
            time.sleep(1)
            dev_b.write(bytes([1<<4]))
            time.sleep(1)
            dev_b.write(bytes([1<<5]))
            time.sleep(1)
            dev_b.write(bytes([0x00]))

        # Toggle GPIO pins on Port A
        with Device(device_id=None, interface_select=1) as dev_a:  # Port A (interface 1)
            dev_a.baudrate = 9600
            dev_a.ftdi_fn.ftdi_set_bitmode(0x15, 0x01)  # Set all pins as output

            dev_a.write(bytes([1<<4]))
            time.sleep(1)
            dev_a.write(bytes([1<<2]))
            time.sleep(1)
            dev_a.write(bytes([1<<0]))
            time.sleep(1)
            dev_a.write(bytes([0x00]))

        

    except FtdiError as e:
        print(f"FTDI device error: {e}")

if __name__ == "__main__":
    toggle_gpio_pins()

