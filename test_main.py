# -*- coding: utf-8 -*-
import pytest

from dingus import Dingus
import editdistance

from main import words_from_tsv, Word, words_in_order

def test_it_gets_words_from_tsv():
    words = words_from_tsv('fixtures/test.csv')
    assert len(words) == 11
    assert words[0].word == u'solenizant'
    assert words[1].word == u'solenizantka'
    assert u'person celebrating' in words[1].translation
    assert words[2].word == u'nieufność'
    assert words[7].translation == u'breakwater'

def test_words_in_order_calls_solve_on_tsp_solver():
    words = [Word('example', 'test')]
    tsp_solver_stub = Dingus('root')
    words_in_order(words, tsp_solver_stub)
    assert tsp_solver_stub.calls('solve', words, editdistance.eval)
