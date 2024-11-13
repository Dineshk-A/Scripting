class Solution:
    def two_sums(nums: list[int],target: int) -> list[int]:
        index_map = {}
        result = []

        for i,n in enumerate(nums):
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i

        return result
    
nums = [2,7,11,13]
target = 9 
result = Solution.two_sums(nums , target)
print(result)