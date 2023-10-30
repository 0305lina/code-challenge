# Question

# There are n kids with candies. You are given an integer array candies
# Each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n.
# Result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids
# False otherwise. 
# Multiple kids can have the greatest number of candies.

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 

from typing import List

class Solution:
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        result = [] # 1. Initialize the list to store result
        maxCandies = max(candies) # 2. Find maxCandies from the integer array candies.
        for i in range(len(candies)): # 3. Iterate over candies to compare maxCandies & (candies + extra candies) and add boolean result to answer
            result.append(candies[i] + extraCandies >= maxCandies)
        return result # 4. Return answer
    print(kidsWithCandies([2,3,1,5,6], 3)) # Test Cases



# Time complexity: O(n) => Iteration for finding maxCandies and for comparison
# Space Complexity: O(1) => no extra space other than integers(maxCandies & candy)



