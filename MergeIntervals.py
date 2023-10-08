
def merge(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i][1] >= nums[i+1][0]:
            nums[i+1] = [min(nums[i][0], nums[i+1][0]), max(nums[i][1], nums[i+1][1])]
            nums[i] = None

    j = -1
    i = 0
    while i < len(nums):
        if nums[i] is None and j == -1:
            j = i
        elif nums[i] is not None and j != -1:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1

        i += 1

    i = 0
    while i < len(nums):
        if nums[i] is None: 
            break
        else:
            i += 1
        
    return nums[:i]

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))
