# -*- coding: utf-8 -*-
import codecs
import sys

import editdistance

from tsp import Tsp

def words_from_tsv(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        lines = f.read().split('\n')
    lines = [line.replace('\r', '').split('\t') for line in lines if line]
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
                output.append(Word(w, translation, notes))
        else:
            output.append(Word(word, translation, notes))
    return output

class Word():
    def __init__(self, word, translation, notes=None):
        self.word = word
        self.translation = translation
        self.notes = notes

if __name__ == '__main__':
    tsp_solver = Tsp()
    words = words_from_tsv(sys.argv[1])
    words_in_order = words_in_order(words, tsp_solver)
    lines = ['\t'.join([w.word, w.translation, w.notes]) for w in words_in_order]
    output = '\n'.join(lines)
    with codecs.open(sys.argv[2], 'w', 'utf-8') as f:
        f.write(output)
