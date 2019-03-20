# aiy-vision-image-capture
Simple continuous photo capture script for Google AIY Vision kit. I made this to gather images for model training. 

Requires leds.py in aiy.vision.leds to have the Color class, enter/exit functions within Leds class and the math module imported. I attached my leds.py file if you need a reference.

When the button is green, press the button to begin taking photos. The button will blink white and the privacy LED will turn on while photos are being gathered.<br />
To pause photo collection, press and hold the button until it flashes red, then release. The button should go back to green.<br />
To end the script, hold down the button until the LED turns off.<br />

In camera.py:<br />
Modify line 12 to change the resolution (default 512x512).<br />
Modify line 25 to change the directory where the photos will be saved.<br />
Modify line 36 to change the time delay between picture captures.
