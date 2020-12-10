import sensor, image, time
import ubinascii
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQCIF)
sensor.skip_frames(time = 2000)
clock = time.clock()
from pyb import UART
uart = UART(3, 115200)
while True:
    clock.tick()
    img = sensor.snapshot()
    cframe = img.compressed(quality=50)
    aaa=ubinascii.b2a_base64(cframe)
    uart.write(aaa)
    uart.write("\r\a")
    print(clock.fps())
