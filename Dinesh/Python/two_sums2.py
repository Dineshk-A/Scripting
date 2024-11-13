def two_sums(nums: list[int] , target: int) ->list[int]:
    result = []
    index_map = {}

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
result = two_sums(nums , target)
print(result)

# Time Complexity
# Since we are iterating the array only once, the time complexity would be O(n).

# Space Complexity
# Since we need a Map of the size of the array, the space complexity would be O(n).
#used here
#break vs exit in python
#enumerate in python
#if , else , break , while , for . function , class etc in python 
#array , list and dictionary