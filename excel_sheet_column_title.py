class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ""
        while (num > 0):
            d = (num - 1) % 26
            num = (num - 1) / 26
            c = chr(ord('A') + d)
            result += c
        return result[::-1]

if __name__ == '__main__':
    res = Solution().convertToTitle(1)
    print(res)
