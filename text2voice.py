import os
import sys 
from gtts import gTTS 
from urllib.request import urlopen 
from bs4 import BeautifulSoup


html_doc = urlopen(sys.argv[1])

f = open("file.txt", "a")
f.write(sys.argv[1])
f.close()

soup = BeautifulSoup(html_doc, 'html.parser')
for EachPart in soup.select('div[class*="chapter-c"]'):
    mytext = EachPart.get_text()


# Language in which you want to convert 
language = 'vi'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("audio.mp3") 

# Playing the converted file 
os.system("afplay audio.mp3") 
