def twoSum(nums, target):
    dict_nums = {}

    for idx, num in enumerate(nums):
        dict_nums[num] = idx
    for idx, num in enumerate(nums):
        if target - num in dict_nums and idx != dict_nums[target - num]:
            return [idx, dict_nums[target - num]]

print(twoSum([2, 7, 11, 15], 9))

# Time Complexity: O(N)
# Space Complexity: O(N)