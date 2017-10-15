#!/usr/bin/python

from PIL import Image
import sys

if len(sys.argv) != 2:
  sys.stderr.write('Usage ./read-image-pixels.py image \n')
  sys.exit(1)
	
im = Image.open(sys.argv[1]) 
pix = im.load()
w,h= im.size #Get the width and hight of the image for iterating over
for x in range(h):
	for y in range(w):
		print pix[y,x]
