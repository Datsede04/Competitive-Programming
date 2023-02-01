class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res=0
        while(tickets[k] != 0):
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return res
                elif tickets[i] != 0:
                    tickets[i]=tickets[i]-1
                    res=res+1;
        return res
