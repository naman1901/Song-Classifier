from extractfeatures import FeatureExtractor
import os

feature_extractor = FeatureExtractor()

for x in ["Classical","Western"]:
	dirs = os.listdir('/'+x+'/')
	dirs = [files for files in dirs if "*.mp3" in files]
	for a in dirs:
		feature_extractor.read_audio(a)
		with open(x+'.txt', 'a') as f:
			f.write(feature_extractor.get_features() + '\n')