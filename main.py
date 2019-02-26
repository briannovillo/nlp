import librosa
import librosa.display
from dtw import dtw
from numpy.linalg import norm
from file import read_file, delete_file, execute_cmd
from record import record_audio

class Word(object):
    def __init__(self, score, name):
        self.score = score
        self.name = name

def compareWordWithDictionary(AUDIO_FILENAME):
    #Loading audio file
    y1, sr1 = librosa.load(AUDIO_FILENAME)

    distances = []
    with open('./dictionary.txt') as f:
        for word in f.read().splitlines():
            execute_cmd('sh ./say.sh '+word)

            # Comparing using espeak Spanish
            y2, sr2 = librosa.load("./normalized/"+ word +".wav")
            #delete_file("./normalized/"+ word +".wav")
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)
            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("Distance between your word and:", word, dist)   # 0 for similar audios
            distances.append(Word(dist,word))

            # Comparing using espeak Spanish2
            y2, sr2 = librosa.load("./normalized2/"+ word +".wav")
            #delete_file("./normalized2/"+ word +".wav")
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)
            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("Distance between your word and:", word, dist)   # 0 for similar audios
            distances.append(Word(dist,word))

            # Comparing using espeak Venezuela
            y2, sr2 = librosa.load("./normalized3/"+ word +".wav")
            #delete_file("./normalized3/"+ word +".wav")
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)
            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("Distance between your word and:", word, dist)   # 0 for similar audios
            distances.append(Word(dist,word))

            # Comparing using espeak Mexican
            y2, sr2 = librosa.load("./normalized4/"+ word +".wav")
            #delete_file("./normalized4/"+ word +".wav")
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)
            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("Distance between your word and:", word, dist)   # 0 for similar audios
            distances.append(Word(dist,word))

            # Comparing using festival
            y2, sr2 = librosa.load("./normalized5/"+ word +".wav")
            #delete_file("./normalized5/"+ word +".wav")
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            librosa.display.specshow(mfcc1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)
            librosa.display.specshow(mfcc2)
            dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
            print("Distance between your word and:", word, dist)   # 0 for similar audios
            distances.append(Word(dist,word))

    distances.sort(key=lambda x: x.score)
    print("You probably said:", distances[0].name)

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)

    # reading audio
    compareWordWithDictionary(AUDIO_FILENAME)

if __name__ == "__main__":
    RecognizeSpeech('record.wav', 5)
