# -*- coding: utf-8 -*-
import codecs

import editdistance

def words_from_tsv(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        lines = f.readlines()
    lines = [line.split('\t') for line in lines]
    words = _make_words(lines)
    return words

def words_in_order(words, tsp_solver):
    return tsp_solver.solve(words, editdistance.eval)

def _make_words(lines):
    output = []
    for word, translation, notes in lines:
        if ', ' in word:
            words = word.split(', ')
            for w in words:
                output.append(Word(w, translation))
        else:
            output.append(Word(word, translation))
    return output

class Word():
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
