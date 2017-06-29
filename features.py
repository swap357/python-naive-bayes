def features(name):
    features = {}
    features['alwayson'] = True
    features['starts_with'] = name.lower()[0]
    features['end_with'] = name.lower()[-1]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features['count(%s)' % letter] = name.lower().count(letter)
        features['has(%s)' % letter] = letter in name.lower()
    return features