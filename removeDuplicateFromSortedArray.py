def removeDuplicates(self, nums):
    
        seen = set()
        i = 0
        last_index = len(nums)

        while(i < last_index):
            if nums[i] in seen:
                nums.append(nums.pop(i))
                last_index -= 1
                continue
            else:
                seen.add(nums[i])
    
            i+=1
        nums = nums[:last_index]
        return len(nums)