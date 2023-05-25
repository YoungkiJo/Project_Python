

# def twoSum(nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# def twoSum2(nums: List[int], target: int) -> List[int]:
def twoSum2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum2(nums, target))
