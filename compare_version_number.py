class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        len1 = len(v1)
        len2 = len(v2)

        len_max = max(len1, len2)
        for i in range(len_max):
            v1_token = 0
            v2_token = 0
            if i < len1:
                v1_token = int(v1[i])
            if i < len2:
                v2_token = int(v2[i])
            if (v1_token > v2_token):
                return 1
            if (v1_token < v2_token):
                return -1
        return 0

if __name__ == '__main__':
    Solution().compareVersion('01', '1')
