import pytube
#link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
print("Enter the link of the youtube video")
link = input()
yt = pytube.YouTube(link)
stream = yt.streams.first()
print("Enter the path of where you want to save it")
path = input()
#path = "C:/Users/divya/Desktop/"
print("What should we name the file as?")
name = input()
stream.download(path, filename = name)
