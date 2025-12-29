# LeetCode 482 - License Key Formatting
# Clean Python Solution | Reverse Traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        res = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1

            if count == k:
                res.append("-")
                count = 0

        if res and res[-1] == "-":
            res.pop()

        return "".join(res[::-1])
