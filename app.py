from urllib.request import urlopen
textpage=urlopen("https://www.python.org/downloads/")

print(textpage.read()) 