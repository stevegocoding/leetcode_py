class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True

        p = 0
        q = len(s) - 1
        while p < q:
            if not s[p].isalnum():
                p += 1
                continue
            if not s[q].isalnum():
                q -= 1
                continue

            if s[p].lower() != s[q].lower():
                return False
            p += 1
            q -= 1
        return True
