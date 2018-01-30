class Vectorizer:
    def __init__(self, article_sents_tokened):
        self.article_sents_tokened = article_sents_tokened
        self.createVectorIndex()
        self.frequencyDictionary()
        self.createFrequencyMatrix()

    def createVectorIndex(self):
        self.vectorIndex = dict()
        ctr = 0
        for sent in self.article_sents_tokened:
            for word in sent:
                if word not in self.vectorIndex.values():
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
        LEN_SENT = len(self.article_sents_tokened)
        for sentence_ctr in range(LEN_SENT):
            for word_index in self.vectorIndex.keys():
                self.frequency_dictionary[(word_index, sentence_ctr)] = self.calculateFrequency(word_index, sentence_ctr)

    def createFrequencyMatrix(self):
        self.frequencyMatrix = []
        LEN_SENT = len(self.article_sents_tokened)
        LEN_WORD = len(self.vectorIndex.keys())
        for i in range(LEN_SENT):
            temp = []
            for j in range(LEN_WORD):
                temp.append(self.frequency_dictionary[(j, i)])
            self.frequencyMatrix.append(temp)
