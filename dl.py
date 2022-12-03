from pytube import YouTube
import time
import os  
import shutil
import glob
from numpy import append
from tqdm import tqdm,trange
from alive_progress import alive_bar
from datetime import date

class yt:
    def __init__(self,link,audio=False):
        self.url=link
        self.ytbVid=YouTube(self.url)
        self.title=self.ytbVid.title
        self.ytbVid.register_on_progress_callback(self.downloadProgress)
        if(audio!=False):
            self.type=audio
            self.itag=251
            self.stream=self.ytbVid.streams.get_by_itag(self.itag)
        
    def getType(self):
        wrongType=True
        while(wrongType==True):
            self.type=input("Entrer video ou audio pour choisir un format:")
            if(self.type=="video" or self.type=="audio"):
                wrongType=False
            else:
                print("Error when trying to enter the type of the file.")
            if(wrongType==False):
                break
            
    def printStreams(self,type):
        if(type=="video"):
            for stream in self.ytbVid.streams.filter(video_codec="vp9"):
                print(" "+str(stream))
        else:
            for stream in self.ytbVid.streams.filter(only_audio=True):
                print(" "+str(stream))
            
    def getStreams(self):
        wrongItag=True
        while(wrongItag==True):
            self.itag=input("Entrer l'itag de la qualité vidéo que vous voulez:")
            if(self.type=="video"):
                if(self.itag=="308" or self.itag=="315" or self.itag=="303" or self.itag=="302" or self.itag=="244" or self.itag=="243" or self.itag=="242" or self.itag=="278" or self.itag=="313" or self.itag=="271" or self.itag=="248" or self.itag=="247" or self.itag=="244" or self.itag=="243" or self.itag=="242"):
                    wrongItag=False
                else:
                    print("L'itag rentrer est n'existe pas. Veuillez en rentrer un autre.")
            else:
                if(self.itag=="139" or self.itag=="140" or self.itag=="249" or self.itag=="250" or self.itag=="251"):
                    wrongItag=False
                else:
                    print("L'itag rentrer est n'existe pas. Veuillez en rentrer un autre.")
                
            if(wrongItag==False):
                self.stream=self.ytbVid.streams.get_by_itag(self.itag)
                break
    def downloadProgress(self,file,stream,bytes_remaining):
        lastPercent=0
        bytes_dowmnload=self.stream.filesize - bytes_remaining
        percent=bytes_dowmnload * 100 / self.stream.filesize - lastPercent
        
        with alive_bar(100) as bar:
            os.system("clear")
            for i in range(round(percent)):
                bar()
        
        
YTlist=[]
index=0
conditionConfig=""

print("Bonjour")

url=""
while(url!="X"):
    url=input("Entrer le lien de votre vidéo ou taper X:")
    if url=="X":
        print("Début du téléchargement.")
        resfolder=input("Voulez vous créer un dossier o/n:")
        currentDate=date.today().strftime('%d-%m-%Y')
        if(resfolder=="o" and os.path.isdir(currentDate)==False):
            os.system(f'mkdir {currentDate}')
            os.system(f'cd {currentDate}')
        break
    else:
        if(index!=0 and conditionConfig=="" ):
            conditionConfig=input("Gardez les mêmes paramètres o/n:")
        if(conditionConfig=="o"):
            object=yt(url)
            if(isinstance(YTlist[index-1],list)):
                object.type=YTlist[index-1][0].type
                object.stream=object.ytbVid.streams.get_by_itag(YTlist[index-1][0].itag)
            else:
                object.type=YTlist[index-1].type
                object.stream=YTlist[index-1].stream
            if(object.type=="video"):
                video=[]
                video.append(object)
                audio=yt(video[0].url,True)
                video.append(audio)
                YTlist.append(video)
            else:
                YTlist.append(object)
            index+=1
        else:
            object=yt(url)
            object.getType()
            object.printStreams(object.type)
            object.getStreams()
            if(object.type=="video"):
                video=[]
                video.append(object)
                audio=yt(video[0].url,True)
                video.append(audio)
                YTlist.append(video)
            else:
                YTlist.append(object)
            index+=1


for i in range(len(YTlist)):
    if(isinstance(YTlist[i],list)): #return true if its a list
        v=0
        for v in range(2):
            try:
                YTlist[i][v].stream.download()
            except:
                print("Erreur dans le telechargement du fichier.")
                YTlist[i][v].printStreams(YTlist[i][v].type)
                YTlist[i][v].getStreams()
                YTlist[i][v].stream.download()
            title=glob.glob("*.webm")[0];
            if(v==0):
                os.rename(title,"video.mp4")
            else:
                os.rename(title,"audio.mp3")
        os.system(f'ffmpeg -i video.mp4 -i audio.mp3 -c copy output.mp4')
        os.system("clear")
        os.remove('video.mp4')
        try:
            os.remove('audio.mp3')
        except:
            print("Erreur, probleme dans la supression de audio.mp3.")
        title=YTlist[i][0].title+".mp4"
        os.system(f'mv output.mp4 "{title}"')
    else:
        YTlist[i].stream.download()
    
if(os.path.isdir(currentDate)): #move files if folder exist
    videos=glob.glob("*.mp4")
    audios=glob.glob("*.mp3")
    for i in range(len(videos)):
        os.system(f'mv "{videos[i]}" {currentDate}')
    for i in range(len(audios)):
        os.system(f'mv "{audios[i]}" {currentDate}')
        
print("Finit")