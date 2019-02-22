import librosa
import librosa.display
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm

def makeSubtitleLineTime(fromFile, toFile):
    #Loading audio files
    y1, sr1 = librosa.load(fromFile)
    y2, sr2 = librosa.load(toFile)

    #Showing multiple plots using subplot
    plt.subplot(1, 2, 1)
    mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
    librosa.display.specshow(mfcc1)

    plt.subplot(1, 2, 2)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    librosa.display.specshow(mfcc2)

    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    print("The normalized distance between the two : ", fromFile, toFile, dist)   # 0 for similar audios

    plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
    plt.plot(path[0], path[1], 'w')   #creating plot for DTW

    plt.show()  #To display the plots graphically



makeSubtitleLineTime('./raw/woman/harina.mp3', './normalized/harina.wav')
makeSubtitleLineTime('./raw/woman/harina.mp3', './normalized/marina.wav')
makeSubtitleLineTime('./raw/woman/harina.mp3', './normalized/manzana.wav')
makeSubtitleLineTime('./raw/woman/harina.mp3', './normalized/banana.wav')
