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
    distance = tsp._compare(word1, word1, editdistance.eval)
    assert distance == 9999

def test_it_makes_distance_matrix():
    matrix = tsp._distance_matrix(words, editdistance.eval)
    assert len(matrix) == 4
    assert len(matrix[0]) == 4
    assert matrix[1][1] == 9999
    assert matrix[0][1] == 5

def test_it_makes_concorde_file_string():
    string = tsp._concorde_file_string([
        [9999, 1, 2, 5],
        [1, 9999, 2, 5],
        [6, 1, 9999, 5],
        [7, 1, 2, 9999],
    ])
    assert '\n9999 1 2 5\n1 9999 2 5\n6 1 9999 5\n7 1 2 9999\n' in string
    assert 'NAME: blah' in string
    assert '\nTYPE: TSP\n' in string
    assert '\nCOMMENT: blah' in string
    assert '\nDIMENSION: 4\n' in string
    assert '\nEDGE_WEIGHT_TYPE: EXPLICIT\n' in string
    assert '\nEDGE_WEIGHT_FORMAT: FULL_MATRIX\n' in string
    assert '\nEDGE_WEIGHT_SECTION\n' in string
    assert '\nEOF' in string

def test_it_reorders_words_based_on_concorde_output():
    with open('fixtures/output.sol', 'r') as f:
        output = f.read()
    print output
    result = tsp._match_words_to_concorde_output(output, [word1, word2, word3, word4, Word('', ''), Word('', ''), Word('', ''), Word('', ''), Word('', ''), Word('', ''), Word('', '')])
    assert len(result) == 11
    assert result[0] == word1
    assert result[6] == word4

