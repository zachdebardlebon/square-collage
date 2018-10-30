from PIL import Image
import random
import sys

size = 100, 100
degrees = [0, 90, 180, -90]

filename = sys.argv[1]
image = Image.open(filename)
image.thumbnail(size, Image.ANTIALIAS)

collage = Image.new('RGB', (700, 700))
x, y = 0, 0
for col in range(7):
	for row in range(7):
		collage.paste(image.rotate(degrees[random.randint(0, 3)]), (x, y))
		y += 100
	x += 100
	y = 0
collage.save(filename.split('.')[0] + "_collage.png")
