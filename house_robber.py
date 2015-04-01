class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        a = 0
        b = 0
        for i in range(len(num)):
            if i % 2 == 0:
                a = a + num[i]
                a = max(a, b)
            else:
                b = b + num[i]
                b = max(a, b)
        return max(a, b)


class Solution2:
    # DP
    # dp(i) = max( dp(i-2) + a[i], dp(i-1) )
    def rob(self, num):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        if len(num) == 2:
            return max(num[0], num[1])
        # cache two results: m => dp(i-1) and n => dp(i-2)
        n = num[0]
        m = max(num[0], num[1])

        result = 0
        for i in range(2, len(num)):
            result = max(m, n + num[i])
            n = m
            m = result
        return result
