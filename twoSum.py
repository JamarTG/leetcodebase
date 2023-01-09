class Solution(object):
    """"""

    def twoSum(self, nums, target):
        
        for i in range(len(nums)-1):
        
            el = nums[i]
        
            for j in range(i+1,len(nums)):
        
                sec_el = nums[j]
                _sum = el + sec_el

                if _sum == target:
                    return [i,j]