class Solution(object):
    """
    # we were required to convert roman numerals to integer

    # my solution
    # there is one trick to this and its that moving from left to right if the value of a letter
    # -is larger than the next, it means we need to subtract them
    # otherwise its just addition


    """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        total = 0
        index = 0

        while index < len(s):
         
            curr_letter = s[index]
            

            if index < len(s)-1:

                next_letter = s[index+1]
                
                if  index != len(s)-1 and d.get(curr_letter) < d.get(next_letter):
                    
                    curr_val = d.get(curr_letter)
                    next_val = d.get(next_letter)

                    total += next_val - curr_val
                    index +=2
                
                else:
                    total += d.get(curr_letter)
                    index +=1
    
            else:
                total += d.get(curr_letter)
                index +=1
        return total