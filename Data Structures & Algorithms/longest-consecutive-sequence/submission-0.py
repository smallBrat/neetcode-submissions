class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        longest = 0

        for num in s:
            if num - 1 not in s:
                next_element = num + 1
                length = 1
                while next_element in s:
                    next_element += 1
                    length += 1
                longest = max(longest, length)

        return longest