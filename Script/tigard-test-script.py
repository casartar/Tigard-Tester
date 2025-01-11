from pylibftdi import Device
from time import sleep

# Define GPIO pins
PIN_MASK = 0xFF  # All 8 GPIO pins (bitmask)
TOGGLE_PIN = 0x01  # Pin to toggle (GPIO 0)

# Open the FT2232 device
try:
    with Device() as dev:
        # Set direction: 1 for output, 0 for input
        dev.baudrate = 9600  # Set baud rate (optional, not critical for GPIO)
        dev.ftdi_fn.ftdi_set_bitmode(PIN_MASK, 0x01)  # Bit-bang mode with all pins as output

        print("Toggling GPIO...")
        while True:
            # Set the pin high
            dev.write(bytes([TOGGLE_PIN]))
            print("Pin HIGH")
            sleep(0.5)

            # Set the pin low
            dev.write(bytes([0x00]))
            print("Pin LOW")
            sleep(0.5)

except Exception as e:
    print(f"Error: {e}")
