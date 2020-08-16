import sys

from PIL import Image

Ascii_character = Ascii_Character = ['.', ',', '*', '+', '-', '@', '#', '0', 'S', '%', '?', ';', ':']


class CharImage():

    def __init__(self, path):
        self.path = path  # path for loading file
        self.image_obj = self.load_image()  # converting image into object of type PngImagePlugin.PngImageFile
        self.pixeled_image = ''
        self.scale = 50  #

    def load_image(self):
        return Image.open(self.path)

    def resize(self, new_width=50):
        self.width = new_width
        old_width, old_height = self.image_obj.size
        aspect_ratio = float(old_height) // float(old_width)
        if aspect_ratio <= 0:  # resolving error for image having width greater than height
            new_height = old_height // 2
        else:
            new_height = int(aspect_ratio * new_width)
        new_dimensions = (self.width, new_height)
        self.image_obj = self.image_obj.resize(new_dimensions, reducing_gap=10)

    def greyscale_image(self):
        self.image_obj = self.image_obj.convert('L')  # u can use P for platting and RGB also

    def modify(self):
        pixels = list(self.image_obj.getdata())  # return an internal datatype and values are flattened
        new_pixels = [Ascii_Character[pixel_value // self.scale] for pixel_value in
                      pixels]  # use a more visible character at pixel_value  // self.scale index
        self.pixeled_image = ''.join(new_pixels)  # returng a long line of characters

    def show_image(self):
        new_image = [self.pixeled_image[index: index + self.width] for index in
                     range(0, len(self.pixeled_image), self.width)]  # making a list of all lines in text image
        print('\n'.join(new_image))  # seperating all lines by '\n' and making a one line


path = sys.argv[1]
image = CharImage(path)
image.load_image()
image.resize(30)
image.greyscale_image()
image.modify()
image.show_image()
