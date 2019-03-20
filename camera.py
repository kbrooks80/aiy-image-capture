from picamera import PiCamera
from gpiozero import Button
from aiy.vision.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from time import sleep

button = Button(23, hold_time=2, hold_repeat=False)
camera = PiCamera()
leds = Leds()

print('Script starting...')

camera.resolution = (512, 512)
sleep(2)
camera.start_preview()

while True:
    try:
        if button.is_held is True:
            raise KeyboardInterrupt
        else:
            leds.update(Leds.rgb_on(Color.GREEN))
            button.wait_for_press()
            leds.pattern = Pattern.blink(2000)
            leds.update(Leds.privacy_on(5))
            for i in camera.capture_continuous('/home/pi/images/'+'tire{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
                print('Captured %s' % i)
                if button.is_held is True:
                    leds.pattern = Pattern.blink(300)
                    leds.update(Leds.privacy_off())
                    leds.update(Leds.rgb_pattern(Color.RED))
                    sleep(2)
                    leds.update(Leds.rgb_on(Color.GREEN))
                    break
                else:
                    leds.update(Leds.rgb_pattern(Color.WHITE))
                    sleep(2)
                    continue
    except KeyboardInterrupt:
        leds.reset()
        camera.stop_preview()
        break
