def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            temp = nums[i] + nums[j]
            if temp == target:
                return [i,j]
    return 0

print(twoSum([2,7,11,15], 13))