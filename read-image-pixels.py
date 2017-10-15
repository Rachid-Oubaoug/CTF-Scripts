from PIL import Image
import sys

im = Image.open(sys.argv[1]) #Can be many different formats.
pix = im.load()
w,h= im.size #Get the width and hight of the image for iterating over
for x in range(h):
	for y in range(w):
		print pix[y,x]
