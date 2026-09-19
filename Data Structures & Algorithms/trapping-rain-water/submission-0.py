class Solution:
    def trap(self, height: List[int]) -> int:
        
        l_wall = 0
        r_wall = 0
        n = len(height)

        max_l = [0] * n
        max_r = [0] * n

        for i in range(n):
            j = - i - 1
            max_l[i] = l_wall
            max_r[j] = r_wall

            l_wall = max(height[i], l_wall)
            r_wall = max(height[j], r_wall)

        result = 0
        for i in range(n):
            pot = min(max_l[i], max_r[i])
            result += max(0, pot - height[i])

        return result