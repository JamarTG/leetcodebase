class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        s = list(filter(lambda x:x!='',s))
        return len(s[-1])