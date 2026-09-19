class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = 0
        right = n - 1

        area = 0

        for i in range(n):
            curr_area = min(heights[left], heights[right]) * (right - left)
            area = max(area, curr_area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return area