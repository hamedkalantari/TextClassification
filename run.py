from keyword_extractor import KeywordExtractor
from training_text_reader import TrainingTextReader


reader = TrainingTextReader('HAM2-070107.xml')
a = KeywordExtractor(reader.articles[10], 'useless.txt')


print a.article_sents_tokened

class Vectorizer:
    def __init__(self, article_sents_tokened):
        self.article_sents_tokened = article_sents_tokened

    def createVectorIndex(self):
        self.vectorIndex = dict()
        ctr = 0
        for sent in self.article_sents_tokened:
            for word in sent:
                self.vectorIndex[ctr] = word
                ctr += 1

    def calculateFrequency(self, vocabulary_index, sentence_index):
        ctr = 0
        for word in self.article_sents_tokened[sentence_index]:
            if word == self.vectorIndex[vocabulary_index]:
                ctr += 1
        return ctr

    def frequencyDictionary(self):
        self.frequency_dictionary = dict()
        for sentence_ctr in range(len(self.article_sents_tokened)):
            for word_index in self.vectorIndex.keys():
                self.frequency_dictionary[(word_index, sentence_ctr)] = self.calculateFrequency(word_index, sentence_ctr)

    def createFrequencyMatrix(self):
        self.frequencyMatrix = []
        for i in range(LEN_SENT):
            temp = []
            for j in range(LEN_WORD):
                temp.append(self.frequency_dictionary[(j, i)])
            self.frequencyMatrix.append(temp)
