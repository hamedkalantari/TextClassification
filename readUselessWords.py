# -*- coding: utf-8 -*-
import re


class ReadUselessWords:
    def __init__(self, path_to_file):
        self.useless_words = []
        lines = self.read_from_file(path_to_file)

        for line in lines:
            word = self.read_doc_properties(line)
            if word:
                self.useless_words.append(word)

    def read_from_file(self, path_to_file):
        with open(path_to_file) as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def read_doc_properties(entry):
        word = re.sub(r'[\n\s]', "", entry)
        return word
