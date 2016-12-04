from extractfeatures import FeatureExtractor

x = FeatureExtractor()

x.read_audio("audio2.mp3")
print(x.get_features())