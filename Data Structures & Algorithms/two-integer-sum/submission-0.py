class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_dict = {}

        for i in range(len(nums)):
            hash_dict[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in hash_dict and hash_dict[y] != i:
                return [i, hash_dict[y]]
