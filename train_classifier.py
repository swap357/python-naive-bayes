import pickle
from nltk import NaiveBayesClassifier
from features import features

f1 = open("male.txt")
f2 = open("female.txt")

trainer = NaiveBayesClassifier.train
namelist = ([(name, 'male') for name in f1] +
                [(name, 'female') for name in f2])

train = namelist[:5000]

classifier = trainer( [(features(n), g) for (n, g) in train] )

with open('classifier.pickle', 'wb') as outfile:
    pickle.dump(classifier, outfile)
    outfile.close()

