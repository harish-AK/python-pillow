from PIL import Image,ImageDraw,ImageFont

file=r'sample.jpeg'
text='P-B'
image = Image.open(file)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=36)
#Positioning Text
textwidth, textheight = draw.textsize(text, font)
width, height =image.size 
x=width/2-textwidth/2
y=height-textheight-300
draw.text((x,y), text, font=font)
image.save('new.jpeg')
