class Tsp():
    def __init__(self):
        return

    def solve(self, words, distance_function):
        matrix = self.distance_matrix(words, distance_function)

    def _compare(self, word1, word2, distance_function):
        return distance_function(word1.word, word2.word)

    def _distance_matrix(self, words, distance_function):
        l = len(words)
        matrix = [[None for x in range(l)] for x in range(l)]
        for i, n in enumerate(words):
            for j, m in enumerate(words):
                matrix[i][j] = self._compare(n, m, distance_function)
        return matrix
