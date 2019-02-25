import librosa
import librosa.display
from dtw import dtw
from numpy.linalg import norm
from file import read_file, delete_file, execute_cmd
from record import record_audio

def compareWordWithDictionary(AUDIO_FILENAME):
    #Loading audio file
    y1, sr1 = librosa.load(AUDIO_FILENAME)

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
            print("Distance between your word and:", line, dist)   # 0 for similar audios

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)

    # reading audio
    compareWordWithDictionary(AUDIO_FILENAME)

if __name__ == "__main__":
    while True:
        RecognizeSpeech('record.wav', 5)
