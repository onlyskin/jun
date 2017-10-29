Jun is a program for putting lists of words in to an order based on their
similarity to the other words in the list.

Jun is set up to work with vocab lists exported from Anki, and as such takes a
tsv file. The file must have three columns, the first is the words which will
be compared for similarity, the second is the translation for those words, the
third is a notes field for the word.

The idea behind Jun is that studying vocabulary lists in an order based around
how similar words are to each other may be an interesting or helpful order to
study them as while studying you have the chance to make sure you see similar
words near to each other and can be less likely to confuse them.

To install:

```
brew tap homebrew/science
brew install concorde
```

To run Jun:

```
python main.py INPUT_FILE OUTPUT_FILE
```

(This will read a tsv file with three columns (WORD, TRANSLATION, NOTES), and
output the same lines reordered by similarity of WORD.)

To run the tests:

```
pytest
```
