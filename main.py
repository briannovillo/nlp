import librosa
import librosa.display
from dtw import dtw
from numpy.linalg import norm
from file import read_file, delete_file, execute_cmd

def compareWordWithDictionary(word):
    #Loading audio file
    y1, sr1 = librosa.load("./raw/man/"+word+".mp3")

    with open('./dictionary.txt') as f:
        for line in f.read().splitlines():
            execute_cmd('sh ./say.sh '+line)

            y2, sr2 = librosa.load("./normalized/"+ line +".wav")
            delete_file("./normalized/"+ line +".wav")

            #Computing MFCC values
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)

            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)

            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("The normalized distance between the two : ", word, line, dist)   # 0 for similar audios

compareWordWithDictionary('harina')
