# -*- coding: utf-8 -*-
import pytest

from main import words_from_tsv

def test_it_gets_words_from_tsv():
    words = words_from_tsv('fixtures/test.csv')
    assert len(words) == 11
    assert words[0].word == u'solenizant'
    assert words[1].word == u'solenizantka'
    assert u'person celebrating' in words[1].translation
    assert words[2].word == u'nieufność'
    assert words[7].translation == u'breakwater'
