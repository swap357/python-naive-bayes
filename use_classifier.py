import pickle
from features import features

f = open('classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

classifier.show_most_informative_features(n=10)
print "Classifier result: " + classifier.classify(features("Swapnil"))
