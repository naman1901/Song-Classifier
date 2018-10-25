from python_speech_features import mfcc
from python_speech_features import delta
# import scipy.io.wavfile as wav
import subprocess as sp
import numpy as np

FFMPEG_PATH = "C:\Program Files\FFMPEG\\bin\\ffmpeg.exe"


class FeatureExtractor(object):

    def __init__(self):
        self.raw_audio = None
        self.mfcc = None
        self.d_mfcc = None
        self.audio_features = None

    def read_audio(self, file):
        # print("1")
        self.raw_audio = None
        self.mfcc = None
        self.d_mfcc = None
        self.audio_features = None
        command = [FFMPEG_PATH,
                   '-i', file,
                   '-f', 's16le',
                   '-acodec', 'pcm_s16le',
                   '-ar', '16000',
                   '-ac', '1',
                   '-']
        # print("2")
        pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE, bufsize=10**8)
        # print("3")
        self.raw_audio = pipe.stdout.read()
        pipe.terminate()
        print("Read %s - Length of sample array: %d" % (file, len(self.raw_audio)))
        # (x, wavfile) = wav.read(file)
        self.raw_audio = np.fromstring(self.raw_audio, dtype="int16")
        print(self.raw_audio)
        # print(wavfile)

    def get_mfcc_features(self):
        # if(self.mfcc==None):
        self.mfcc = mfcc(self.raw_audio, 16000)
        # print(len(self.mfcc[50]))
        # print(self.mfcc)
        # return self.mfcc

    '''Work in progress :P
     def get_delta_mfcc_features(self):
         if(self.d_mfcc==None):
             if(self.mfcc==None):
                 self.get_mfcc_features()
             self.d_mfcc = delta(self.mfcc, 1)
         print(self.d_mfcc)
        return self.d_mfcc'''

    def build_features(self):
        if(self.mfcc==None):
            self.get_mfcc_features()
        self.audio_features = np.zeros(13, dtype="int16")
        l = len(self.mfcc)
        for x in self.mfcc:
            for i in range(0,13):
                self.audio_features[i] += x[i]
                # print(x[i])
        for i in range(0,13):
            self.audio_features[i] /= l

    def get_features(self):
        if(self.audio_features==None):
            self.build_features()
        return self.audio_features
