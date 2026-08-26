import re
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        for oper in operations:
            if bool(re.match(r"^[-+]?\d+(\.\d+)?$", oper)):
                record.append(int(oper))
            if oper == '+':
                entryOne = record[-1]
                entryTwo = record[-2]
                record.append(entryOne + entryTwo)
            if oper == 'C':
                record.pop()
            if oper == 'D':
                entryOne = record[-1]
                record.append(entryOne * 2)

        for i in record:
            result += i

        return result



        
        