# Hotel-Reviews-Classifier

This is a Naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative. The NB classifier has been implemented by using the word tokens as features for classification.

This repository has two programs: nblearn.py will learn a naive Bayes model from the training data (train-text.txt and train-labels.txt), and nbclassify.py will use the model (nbmodel.txt) to classify new data in test.txt. Output is stored in nboutput.txt

The training data consists of two files: 

(1) A text file train-text.txt with a single training instance (hotel review) per line. The first token in the each line is a unique 20-character alphanumeric identifier, which is followed by the text of the review.

(2) A label file train-labels.txt with labels for the corresponding reviews. Each line consists of three tokens: a unique 20-character alphanumeric identifier corresponding to a review, a label truthful or deceptive, and a label positive or negative.
