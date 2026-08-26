class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        for oper in operations:
            if oper == '+':
                entryOne = record[-1]
                entryTwo = record[-2]
                record.append(entryOne + entryTwo)
                continue
            if oper == 'C':
                record.pop()
                continue
            if oper == 'D':
                entryOne = record[-1]
                record.append(entryOne * 2)
                continue
            record.append(int(oper))

        for i in record:
            result += i

        return result



        
        