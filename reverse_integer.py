class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        sign = -1 if x < 0 else 1
        n = abs(x)
        max_int = 2 ** 32
        while (n != 0):
            result = result * 10 + n % 10
            if (result > max_int):
                return 0
            n = n / 10
        return result * sign


if __name__ == "__main__":
    result = Solution().reverse(1534236469)
    print(result)
