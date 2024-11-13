def two_sums(nums , target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i ,j]
            
    return []

nums = [2,7,11,13]
target = input("enter the target:")
#input(prompt)
result = two_sums(nums,target)

print(result)

    