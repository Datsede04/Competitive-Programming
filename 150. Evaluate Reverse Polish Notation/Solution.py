class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        for i in tokens:
            if i not in "*/+-":
                temp.append(i)
            else:
                second = temp.pop()
                first = temp.pop()
                if i =="+":
                    result = int(first) + int(second)
                    temp.append(result)
                elif i =="-":    
                    result = int(first) - int(second)
                    temp.append(result)
                elif i =="*":    
                    result = int(first) * int(second)
                    temp.append(result)
                elif i =="/":    
                    result = int(first) / int(second)
                    temp.append(result)
        return int(temp.pop())