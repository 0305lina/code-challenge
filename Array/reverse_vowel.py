# Given a string s, reverse only all the vowels and return string.
# Vowels are 'a', 'e', 'i', 'o', 'u'
# Vowels can appear in both lower and upper cases, more than once.

# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(s: str) -> str:

        s = list(s) # Change String into Arraylist
        vowel= 'aeiouAEIOU' # Initiate the vowel

        low = 0 # Set two pointers for low and high for the given term
        high = len(s) - 1

        while low < high: # Go over while loop until low and high doesn't count the same string
            while low < high and s[low] not in vowel:
                low += 1
            while low < high and s[high] not in vowel:
                high -= 1
            s[low], s[high] = s[high], s[low] # low 와 high에서 vowel 이 찾아질 경우 reverse하기 
            low += 1
            high -= 1
        return "".join(s) # Arraylist를 join 써서 다시 string으로 합쳐주기
    
    print(reverseVowels('Hello')) # Test Case

# Time complexity: O(n^2): We used nested while loop
# Space complexity: O(n): We created new array to store string