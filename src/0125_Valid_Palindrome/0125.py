class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 将字符串中的字母按顺序拿出来
        # 并且将大写字母转化成小写添加到一个新的字符串中
        # 判断是否是回文字符串
        s_filter = ''.join(filter(str.isalnum,s)).lower()
        return s_filter[::-1] == s_filter


if __name__ == '__main__':
    a = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(a))

