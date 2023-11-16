import time
import os
import fetchposts as fp
import mkimg as Maker

PostCount = input("How many top posts should be exported?: ")
if not os.path.isfile("subreddits.txt"):
	Makenew = str(input("Do you want to make a new automatic subreddits file?: "))
	Subreddits = str(input("Enter subreddits of choice (Separated by commas) : "))
	SplitReddits = Subreddits.split(",")
	if Makenew == "y" or Makenew == "Y":
		NewFile = open("subreddits.txt", "w")
		for i in SplitReddits:
			NewFile.newline(i)
		Newfile.write()
	FuncSubreddits = SplitReddits
else:
	Subreddits = open("subreddits.txt","r")
	Subreddits = Subreddits.read().split("\n")
	FuncSubreddits = Subreddits
CompleteData = fp.GetPosts(FuncSubreddits,int(PostCount))
Maker.MakeImg(CompleteData)




