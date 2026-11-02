class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate area with current pair
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)
            
            # Move the pointer pointing to the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area