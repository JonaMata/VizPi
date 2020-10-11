import board
import neopixel
import time
import colorsys
pixels = neopixel.NeoPixel(board.D18, 30*5)

hue = 0
deltaHue = 0.05
timeDeltaHue = 0.01

while True:
	color = colorsys.hsv_to_rgb(hue,1,1)
	pixels.fill((int(color[0]*100),int(color[1]*100),int(color[2]*100)))
	pixels.show();
	hue+=timeDeltaHue
