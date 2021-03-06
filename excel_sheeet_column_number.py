class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        for c in s:
            result = result * 26 + ord(c) - ord('A') + 1
        return result
