
#  Converts the videos to mp3
import os 
import subprocess 


files  = os.listdir("Videos")
for file in files:
  #print(file)
  name = file.replace(".mp4","")

  number,text = name.split(".", 1)

  print("Number:", number)
  print("Text :",text)
  subprocess.run(["ffmpeg", "-i", f"Videos/{file}",f"audios/{number}_{text}.mp3"])
 