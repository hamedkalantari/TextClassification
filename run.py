from keyword_extractor import KeywordExtractor
from training_text_reader import TrainingTextReader
from vectorizer import Vectorizer
from vector_normalizer import VectorNormalizer
from inverse_document_frequency import InverseDocumentFrequency


def create_tf_idf(file_path):
    reader = TrainingTextReader(file_path)
    keywords = KeywordExtractor(reader.articles[10], 'useless.txt')
    vector_index = Vectorizer(keywords.article_sents_tokened)
    freq_mat = vector_index.frequencyMatrix
    normalized_vector = VectorNormalizer(freq_mat)
    norm_mat = normalized_vector.l2_norm_matrice
    tf_idf = InverseDocumentFrequency(norm_mat)
    return tf_idf.tf_idf_matrice


training_set_of_tf_idf = create_tf_idf('HAM2-070107.xml')

print training_set_of_tf_idf
