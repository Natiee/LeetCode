class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 字符串中的字母按顺序拿出来
        # 将大写的字母转化为小写字母添加到一个新的字符串中
        # 判断回文字符串
        s_filter = ''.join(filter(str.isalnum,s)).lower()
        return s_filter[::-1] == s_filter


if __name__ == '__main__':
    a = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(a))