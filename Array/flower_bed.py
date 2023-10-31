# You have a long flowerbed
# Some of the plots are planted, and some are not. 
# Flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's
# 0 means empty and 1 means not empty, and an integer n
# Return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule
# False otherwise.

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

from typing import List

class Solution:
    def placeFlower(flowerbed: List[int], n: int) -> bool:
        count = 0 # find the maximum number of flower that can be planted in given array
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: # Check if the flowerbed is 0
                left_empty = (i == 0) or (flowerbed[i-1] == 0) # find the condition where left is empty
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) # find the condition where right is empty
                if left_empty and right_empty: # if left and right is empty,
                    flowerbed[i] = 1 # Change flowerbed into 1
                    count += 1 # Add 1 to the maximum number of flower that can be planted
        return count >= n # Return true if the maximum number of flower that can be planted is bigger than the given n(flowers that need to be planted)
    
    print(placeFlower([1,0,0,0,1], 1))
    
# Time complexity: O(n) => By for loop, go over flowerbed array that has the size n
# Space complexity: O(1) => didn't use extra space other than constant such as count.
