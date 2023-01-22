import os
import configparser
import string
import shutil
from pydub import AudioSegment


class Converter:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def getsourcefiles(self):
        dir_list = os.listdir(self.source)
        return dir_list

    def convertertomp3(self,dir_list):
        for f in dir_list:
            m4a=os.path.join(self.source,f)
            mp3=os.path.join(self.target, f.replace(".m4a", ".mp3"))
            if not m4a.endswith(".mp3") and not os.path.exists(mp3):
                wav_audio = AudioSegment.from_file(m4a, format="m4a")
                wav_audio.export(mp3, format="mp3")
            elif os.path.exists(mp3):
                print("El archivo " + mp3 + " ya existe")
            else:
                shutil.copy2(m4a,self.target)
                print("El archivo " + mp3 + " ya es un mp3")


    def run(self):
        dir_list=self.getsourcefiles()
        self.convertertomp3(dir_list)
        #self.test()





if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('./config.ini')
    sourcePath = config['DEFAULT']['sourcePath']
    targetPath = config['DEFAULT']['targetPath']

    converter = Converter(source=sourcePath,target=targetPath)
    converter.run()

