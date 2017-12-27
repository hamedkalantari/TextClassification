# -*- coding: utf-8 -*-
from xml.etree import ElementTree


class TrainingTextReader:
    def __init__(self, path_to_file):
        self.articles = []
        self.read_from_file(path_to_file)
        # print(self.articles)

    def read_from_file(self, path_to_file):
        root = ElementTree.parse(path_to_file).getroot()

        for element in root:
            if element.tag == 'DOC':
                self.articles.append(TrainingTextReader.read_doc_properties(element))

    @staticmethod
    def read_doc_properties(element):
        result = dict()
        for property in element:
            if property.tag == 'CAT' and property.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                result['category'] = property.text
            elif property.tag == 'TEXT':
                result['text'] = property.text
            elif property.tag == 'TITLE':
                result['title'] = property.text
        return result


# TrainingTextReader('/Users/hamed/Desktop/HAM2-070107.xml')
