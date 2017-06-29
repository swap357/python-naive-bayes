import pickle
from features import features

try:
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    classifier.show_most_informative_features(n=10)
    print "Classifier result: " + classifier.classify(features("Swapnil"))

except:
    print "Prepare the classifier using - train_classifier.py and then try to use."

