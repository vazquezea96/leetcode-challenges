def search(nums, target) -> int:
    for num in nums:
        if target in nums:
            return nums.index(target)
        else:
            return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
# Expected: 4
# Output: 4
