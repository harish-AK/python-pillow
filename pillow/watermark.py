
from PIL import Image,ImageDraw,ImageFont
import io

text='P-B'
with open(r'index.webp','rb') as f:
    image = Image.open(f)


    draw=ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=36)
    textwidth, textheight = draw.textsize(text, font)
    width, height =image.size 
    x=width/2-textwidth/2
    y=height-textheight-300
    draw.text((x,y), text, font=font)
    # create buffer
    buf=io.BytesIO()
    #save watermark image to buffer
    image.save(buf,format='JPEG')
# Save the buffer to a file
with open('wate.jpg', 'ab') as f:
    a=f.write(buf.getbuffer())
print('a=',a)


