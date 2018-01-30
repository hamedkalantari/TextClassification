import math
import numpy
from vector_normalizer import VectorNormalizer


class InverseDocumentFrequency:
    def __init__(self, matrice):
        self.tf_matrice = matrice
        self.idf_matrice = []
        self.tf_idf_matrice = []
        self.documents_count = len(matrice)
        self.words_count = len(matrice[0])
        self.idf_of_word = dict()
        self.calculate_idf()
        self.create_idf_matrice()
        self.create_tf_idf_matrice()

    def calculate_idf(self):
        for word_no in range(self.words_count):
            how_many_docs_words_is_in = 0
            for freq in self.tf_matrice:
                if freq[word_no]:
                    how_many_docs_words_is_in += 1
            tmp = float(self.documents_count) / (1 + how_many_docs_words_is_in)
            self.idf_of_word[word_no] = math.log(tmp)

    def create_idf_matrice(self):
        LEN = len(self.idf_of_word.keys())
        for i in range(LEN):
            tmp = []
            for j in range(LEN):
                if i == j:
                    tmp.append(self.idf_of_word[i])
                else:
                    tmp.append(0.0)
            self.idf_matrice.append(tmp)

    def create_tf_idf_matrice(self):
        tmp = numpy.matmul(self.tf_matrice, self.idf_matrice)

        # normalize the result
        norm = VectorNormalizer(tmp)
        self.tf_idf_matrice = norm.l2_norm_matrice
