class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 != p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

