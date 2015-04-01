class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, s, e):
        for x in range(s, (s + e) / 2):
            nums[x] ^= nums[s + e - x - 1]
            nums[s + e - x - 1] ^= nums[x]
            nums[x] ^= nums[s + e - x - 1]

if __name__ == "__main__":
    a = [1, 2]
    k = 1
    Solution().rotate(a, k)
    print(a)
