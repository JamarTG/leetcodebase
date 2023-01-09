class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for charac in s:
            if charac in '[({':
                stk.append(charac)
            elif charac == ']':
                if stk == [] or stk[-1]!='[':
                    return False
                stk.pop()
            elif charac == ')':
                if stk == [] or stk[-1]!='(':
                    return False
                stk.pop()
            elif charac == '}':
                if stk == [] or stk[-1]!='{':
                    return False
                stk.pop()
        return not stk 