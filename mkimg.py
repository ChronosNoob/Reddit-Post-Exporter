import matplotlib
from PIL import Image, ImageDraw, ImageFilter

def MakeImg(CompleteData):
    for subreddit in CompleteData:
        for post in subreddit:
            CurrentData = post 
            print(CurrentData)
            Img = Image.new(mode="RGB", size=(1920,1500))
