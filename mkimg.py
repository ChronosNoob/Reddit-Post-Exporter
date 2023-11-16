import matplotlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import urllib.request

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
            TitleFont = ImageFont.truetype(r'fonts/Roboto-Medium.ttf',162)
            BodyFont = ImageFont.truetype(r'fonts/RedditSans-Regular.ttf',12)
            Draw.text((30,15),Title,(255,255,255),Font=TitleFont)
            if imgurl != False:
                urllib.request.urlretrieve(imgurl,"img.png")
                image = Image.open("img.png")
                
            Canvas.show()
            Canvas.save("image.png")
            break
        break
            
            
