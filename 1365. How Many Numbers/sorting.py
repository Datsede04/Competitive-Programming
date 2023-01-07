class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        size = len(nums)
        result = []
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                elif nums[i]>nums[j] :
                    count+=1
            result.append(count)
            count=0
        return result