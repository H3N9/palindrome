import ast

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum > 0:
                j += 1
            else:
                k -= 1
    return result

threeSum(ast.literal_eval(input()))