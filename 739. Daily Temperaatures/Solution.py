class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        n = len(temperatures)
        result = [0] * n
        s = []

        for i in range(n): 
            while(len(s) != 0 and t[s[-1]]<t[i]):
                result[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return result