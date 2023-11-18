import matplotlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import urllib.request
from txtwrap import wrap_text
import textwrap
import re 
import codecs


def MakeImg(CompleteData):
    for subreddit in CompleteData:
        for post in subreddit:
            CurrentData = post 
            Title = CurrentData[0]
            BodyText = CurrentData[1]
            Author = CurrentData[2]
            imgurl = CurrentData[3]
            Comments = CurrentData[4]
            Canvas = Image.new(mode="RGB", size=(1920,1500), color=(50,50,50))
            Draw = ImageDraw.Draw(Canvas) 
            TitleFontSize = 1
            BodyFontSize = 10
            BodyFont = ImageFont.truetype('bfont.ttf',15)
            Titlefont = ImageFont.truetype("afont.ttf", TitleFontSize)
            img_fraction = 0.90
            while Titlefont.getlength(Title) < img_fraction*Canvas.size[0] and Titlefont.size < 25:
                # iterate until the text size is just larger than the criteria
                TitleFontSize += 1
                Titlefont = ImageFont.truetype("afont.ttf", TitleFontSize)
            Draw.text((30,15),Title,(255,255,255),font=Titlefont)
            offset = 50
            if BodyText:
                #BodyText = BodyText.replace(' ','\n')
                #BodyText = BodyText.replace(r'/\n/g','\n')
                #BodyText = re.sub(r'\r\n', '\n' , BodyText)

                margin = 35
                for line in textwrap.wrap(BodyText, width=275,replace_whitespace=False):
                    print(line)
                    Draw = ImageDraw.Draw(Canvas)
                    Draw.text((margin, offset), line, font=BodyFont, fill="#ffffff")
                    left,top,right,bottom = BodyFont.getbbox(line)
                    width = right - left
                    height = bottom - top
                    print(height)
                    offset += 25
                    Draw.ellipse(((margin,offset),(margin + 5,offset+5)),fill="red", width=5)
                    print(offset)

                #Draw.text((30,100),BodyText,(255,255,255),BodyFont)
            if imgurl != False:
                urllib.request.urlretrieve(imgurl,"img.jpg")
                image = Image.open("img.png")
                Canvas.paste(image,box=(30,offset))
            #Canvas.show()
            Canvas.save("image.png")
            break
        break
            
            
