#Import required Image library
from PIL import Image, ImageDraw, ImageFont
import os

src = os.path.join(os.getcwd(),"travel")
dst = os.path.join(os.getcwd(),"gallery")
#Create an Image Object from an Image

for item in os.listdir(src):
    print(item)
    im = Image.open(os.path.join(src,item))
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = '© ' + "Shakeel"
    font = ImageFont.truetype('Lato-Medium.ttf', 50)
    textwidth, textheight = draw.textsize(text, font)
    # calculate the x,y coordinates of the text
    margin = width/2
    x = width - textwidth - margin
    y = height - textheight - margin
    # draw watermark in the bottom right corner
    draw.text((x, y), text, fill=(150, 150, 150, 15),font=font)
    #im.show()
    #comb = Image.alpha_composite(im, text)
    #Save watermarked image
    im.save(os.path.join(dst, item))
