def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        last_index = len(nums)

        while i < last_index:
            if nums[i] == val:
                nums.append(nums.pop(i))
                last_index -=1
                continue
            else:
                pass
            
            i+=1
        nums = nums[:last_index]
        return len(nums)