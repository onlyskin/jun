class Tsp():
    def __init__(self):
        return

    def solve(self, words, distance_function):
        matrix = self._distance_matrix(words, distance_function)
        file_output = self._concorde_file_string(matrix)

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
