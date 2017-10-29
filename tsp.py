import os
import tempfile
import subprocess
import shutil

class Tsp():
    def __init__(self):
        return

    def solve(self, words, distance_function):
        matrix = self._distance_matrix(words, distance_function)
        concorde_input = self._concorde_file_string(matrix)
        concorde_output = self._run_concorde(concorde_input)
        return self._match_words_to_concorde_output(concorde_output, words)

    def _run_concorde(self, concorde_input):
        cwd = os.getcwd()
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        with open('temp.txt', 'w') as f:
            f.write(concorde_input)
        subprocess.call(['concorde', 'temp.txt'], stdout=None)
        with open('temp.sol', 'r') as f:
            concorde_output = f.read()
        os.chdir(cwd)
        shutil.rmtree(temp_dir)
        return concorde_output

    def _match_words_to_concorde_output(self, output, words):
        order = self._make_order(output)
        return [words[i] for i in order]

    def _make_order(self, output):
        result = output.split('\n')[1:]
        result = ' '.join(result)
        result = result.split(' ')
        result = [int(o) for o in result if o != '']
        return result

    def _compare(self, word1, word2, distance_function):
        if word1.word == word2.word:
            return 9999
        return distance_function(word1.word, word2.word)

    def _distance_matrix(self, words, distance_function):
        l = len(words)
        matrix = [[None for x in range(l)] for x in range(l)]
        for i, n in enumerate(words):
            for j, m in enumerate(words):
                matrix[i][j] = self._compare(n, m, distance_function)
        return matrix

    def _concorde_file_string(self, distance_matrix):
        matrix_string = '\n'.join([' '.join([str(cell) for cell in row]) for row in distance_matrix])
        start = 'NAME: blah\nTYPE: TSP\nCOMMENT: blah\n'\
            'DIMENSION: ' + str(len(distance_matrix)) + '\n'\
            'EDGE_WEIGHT_TYPE: EXPLICIT\n'\
            'EDGE_WEIGHT_FORMAT: FULL_MATRIX\n'\
            'EDGE_WEIGHT_SECTION\n'
        end = '\nEOF'
        return start + matrix_string + end
