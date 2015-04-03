class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(prefix) and j < len(strs[i]):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            if j >= len(prefix) - 1:
                prefix = prefix[0:j]
        return prefix
