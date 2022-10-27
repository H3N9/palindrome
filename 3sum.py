import ast

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            print(nums[i] , nums[j] , nums[k])
            if sum == 0:
                a = [nums[i], nums[j], nums[k]]
                if a not in result:
                    result.append(a)
                k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1
    return result

threeSum(ast.literal_eval(input()))