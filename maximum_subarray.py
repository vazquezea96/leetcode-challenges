def maxSubArray(nums):
    # Dynamic Programming Method

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

    # Slider Window Method

    # max_sum = float('-inf')
    # start = 0
    # end = 0
    # current_sum = 0

    # for i in range(len(nums)):
    #     current_sum += nums[i]

    #     if current_sum > max_sum:
    #         max_sum = current_sum
    #         end = i + 1
        
    #     if current_sum < 0:
    #         current_sum = 0
    #         start = end + 1
    
    # return max_sum

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
print(maxSubArray([1])) # Output: 1
print(maxSubArray([5, 4, -1, 7, 8])) # Output: 23