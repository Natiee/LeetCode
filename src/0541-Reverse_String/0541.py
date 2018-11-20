"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
"""


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        for i in range(0, length, 2 * k):
            if i + k >= length:
                s = s[:i] + s[i:][::-1]
            else:
                s = s[:i] + s[i:i + k][::-1] + s[i + k:]
        return s


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s, k))