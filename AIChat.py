#Keith Flagg
#A basic python chat AI preprocessor 
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy 
import tflearn
import tensorflow as tf
import random
import json
import pickle
import jieba

with open("intents.json",encoding="utf-8") as file:
	data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
	for pattern in intent["patterns"]:
		twords = jieba.lcut(pattern)
		words.extend(twords)
		docs_x.append(twords)
		docs_y.append(intent["tag"])

		if intent["tag"] not in labels:
			labels.append(intent["tag"])
words = [stemmer.stem(w.lower()) for w in words if w != "?"]

words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

output_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
	bag = []

	twords = [stemmer.stem(w) for w in doc]

	for w in words:
		if w in twords:
			bag.append(1)
		else:
			bag.append(0)

	output_row = output_empty[:]
	output_row[labels.index(docs_y[x])] = 1

	training.append(bag)
	output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

with open("data.pickle", "wb") as f:
	pickle.dump((words, labels, training, output), f)

tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape = [None, len(training[0])])
net = tflearn.fully_connected(net,int(len(output[0]) * 4))
net = tflearn.fully_connected(net,int(len(output[0]) / 2))
net = tflearn.fully_connected(net,len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

def training_model(Select_epoch):
	model.fit(training, output, n_epoch = Select_epoch, batch_size = int(len(training) / 100), show_metric = False)
	model.save("model.tflearn")

training_model(int(len(training) * 5))

def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = jieba.lcut(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for sent in s_words:
		for i, w in enumerate(words):
			if w == sent:
				bag[i] = 1

	return numpy.array(bag)

def chat(input_message):
	results = model.predict([bag_of_words(input_message, words)])

	results_index = numpy.argmax(results)
	tag = labels[results_index]
	if results[0, results_index] > 0.6:

		for tg in data["intents"]:
			if tg['tag'] == tag:
				responses = tg['responses']
		return random.choice(responses)

	else: 
		return "{__UNKNOW_REPLY}"