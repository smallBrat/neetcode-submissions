from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        n = len(nums)
        bucket = [0] * (n+1)

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)

        lst = []

        for i in range(n, -1, -1):
            if bucket[i] != 0:
                lst.extend(bucket[i])
            if len(lst) == k:
                break

        return lst