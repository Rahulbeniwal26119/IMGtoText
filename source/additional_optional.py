#optional file for use of PIL and glob
import sys
import glob
from PIL import Image
size = 128 , 128 

#convering an image into the thumbnail

for infile in glob.glob('*.jpeg'):
	file , ext = os.path.splitext(infile)
	im = Image.open(infile)
	im.thumbnail(size)
	im.save(file + ".thumbnail" + "JPEG")

