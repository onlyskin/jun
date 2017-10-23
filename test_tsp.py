import pytest

import editdistance

from main import Word
from tsp import Tsp

tsp = Tsp()
word1 = Word('apple', 'sample')
word2 = Word('orange', 'sample')
word3 = Word('banana', 'sample')
word4 = Word('pear', 'sample')
words = [word1, word2, word3, word4]

def test_it_compares_two_words_by_word_with_distance_function():
    distance = tsp._compare(word1, word2, editdistance.eval)
    assert distance == 5

def test_it_makes_distance_matrix():
    matrix = tsp._distance_matrix(words, editdistance.eval)
    assert len(matrix) == 4
    assert len(matrix[0]) == 4
    assert matrix[1][1] == 0
    assert matrix[0][1] == 5
