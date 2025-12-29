🧩 Problem Statement

Given an integer array nums and an integer k, return True if there are two distinct indices i and j such that:

nums[i] == nums[j]

|i - j| ≤ k

Otherwise, return False.

💡 Approach: Hash Map (Index Tracking)

We use a dictionary to store the last index at which each number appeared.

Why this works:

When a number appears again, we only care about the closest previous occurrence

If the index difference is within k, we immediately return True

🧠 Algorithm Steps

Create an empty dictionary to store number → last index

Traverse the array using enumerate

For each element:

If it already exists in the dictionary:

Check if the index difference is ≤ k

If yes, return True

Update the index of the element in the dictionary

If no valid pair is found, return False

🧪 Example
Input:  nums = [1, 2, 3, 1], k = 3
Output: True

Explanation:
The number 1 appears at indices 0 and 3
|3 - 0| = 3 ≤ k

✅ Python Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}

        for i, n in enumerate(nums):
            if n in dct and i - dct[n] <= k:
                return True
            dct[n] = i

        return False

⏱️ Complexity Analysis

Time Complexity: O(n)
(Single pass through the array)

Space Complexity: O(n)
(Hash map stores elements and their last indices)

⭐ Key Takeaways

Hash maps are ideal for tracking indices

Always update the index to keep the closest occurrence

Early return improves performance

Interview-friendly & optimal solution
