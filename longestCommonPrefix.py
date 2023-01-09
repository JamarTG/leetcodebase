class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 1:
            return strs[0]

        shortest_length = min(map(len,strs))
        
        constring = ''


        for i in range(shortest_length):
            l = strs[0][i]

            for word in strs:
                if word[i] != l:
                    return constring

            constring +=l
        return constring