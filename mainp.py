import glob
from PIL import Image

import os

file_name =('590.jpeg')
im = Image.open(file_name)
rgb_im= im.convert('RGB')
rgb_im.save(str(file_name[:3])+'.jpg')

