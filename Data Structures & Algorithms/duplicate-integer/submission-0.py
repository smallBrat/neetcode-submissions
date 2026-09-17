class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_dict = {}
        for i in nums:
            if i not in hash_dict:
                hash_dict[i] = 0
            else:
                hash_dict[i] += 1

        for i in hash_dict:
            if hash_dict[i] > 0:
                return True
        return False