import math


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        if x == 0:
            return True

        num_digits = int(math.log10(x)) + 1
        for i in range(0, num_digits // 2):
            begin_digit = (x // (10 ** (num_digits - i - 1))) % 10
            end_digit = (x // (10 ** i)) % 10
            if begin_digit != end_digit:
                return False
        return True


if __name__ == '__main__':
    ret = Solution().isPalindrome(10)
    print ret
