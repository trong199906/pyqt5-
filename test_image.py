import math
from PIL import Image, ImageDraw
w, h = 7000, 7000
shape = [(3500, 3500), (w - 3000, h - 3000)]

# creating new Image object
img = Image.new("RGB", (w, h))

# create rectangle image
img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill="#ffff33", outline="red")
img.show()
img.save("output.jpg", "JPEG")