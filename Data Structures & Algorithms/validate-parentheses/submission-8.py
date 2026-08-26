class Solution:
    def isValid(self, s: str) -> bool:
        expected = []
        # openBrakets = ['(','[','{']
        # closeBrakets = [')',']','}']
        valid = True
        for i in s:
            if i in '([{':
                if i == '(':
                    expected.append(1)
                if i == '[':
                    expected.append(2)
                if i == '{':
                    expected.append(3)
            if i in ')]}':
                if len(expected) == 0:
                    return False
                if i == ')':
                    if expected[-1] != 1:
                        valid = False

                if i == ']':
                    if expected[-1] != 2:
                        valid = False

                if i == '}':
                    if expected[-1] != 3:
                        valid = False
                expected.pop()
        if len(expected) > 0:
            return False
        return valid


        