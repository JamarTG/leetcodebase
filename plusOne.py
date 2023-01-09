def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        curr_index = len(digits) - 1

        while(curr_index >= 0):
            curr_val = digits[curr_index]
            res_digit = 0
            gross_sum = carry + curr_val
            
            if gross_sum == 10:
                carry = 1
                digits[curr_index] = 0
            else:
                digits[curr_index] = gross_sum
                carry = 0
            curr_index -= 1
        
        if carry == 1:
            return [1] + digits
        else:
            return digits