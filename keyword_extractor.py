# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *
from readUselessWords import ReadUselessWords


class KeywordExtractor:
    def __init__(self, article_obj, useless_words_addr):
        self.useless_words = ReadUselessWords(useless_words_addr).useless_words
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()

        article_text = article_obj['text']
        article_text = self.normalize_text(article_text)
        article_sents = self.split_sentence(article_text)
        self.article_sents_tokened = self.remove_useless_words(article_sents)

    def normalize_text(self, text):
        return self.normalizer.normalize(text)

    def split_sentence(self, text):
        return sent_tokenize(text)

    def split_words(self, text):
        return word_tokenize(text)

    def remove_useless_words(self, article_sents):
        article_sents_tokened = []
        for sent in article_sents:
            sent_words = self.split_words(sent)
            for word in sent_words:
                if word not in self.useless_words:
                    article_sents_tokened.append(self.split_words(sent))
        return article_sents_tokened
