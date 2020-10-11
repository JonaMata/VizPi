import board
import neopixel
import time
import colorsys
pixels = neopixel.NeoPixel(board.D18, 60*2, auto_write=False)

hue = 0
deltaHue = 0.1
timeDeltaHue = 0.05

while True:
	for i in range(60*2):
		color = colorsys.hsv_to_rgb(hue+i*deltaHue,1,1)
		pixels[i] = (int(color[0]*100),int(color[1]*100),int(color[2]*100))
		
	pixels.show();
	hue+=timeDeltaHue
	time.sleep(0.1)
