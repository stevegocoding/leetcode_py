class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        sum = 0
        sign = 1
        if len(str) == 0:
            return 0
        p = 0
        while p < len(str) and str[p].isspace():
            p += 1
        if str[p] == '-' or str[p] == '+':
            sign = -1 if str[p] == '-' else 1
            p += 1
        while p < len(str) and str[p].isdigit():
            digit = int(str[p])
            if sum * 10 <= INT_MAX:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                elif sign == -1:
                    return INT_MIN
            if sum + digit <= INT_MAX:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                elif sign == -1:
                    return INT_MIN
            p += 1
        return sign * sum
