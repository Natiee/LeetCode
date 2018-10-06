class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # 直接用内置函数lower即可
        return str.lower()

if __name__ == '__main__':
    print(Solution().toLowerCase('HELLO'))