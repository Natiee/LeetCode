"""
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤纪录判断他是否会被奖赏。
"""


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') < 2 and s.count('LLL') < 1: # count(),统计字符串里某个字符出现的次数

            return True
        return False


if __name__ == '__main__':
    s = 'PPALLP'
    print(Solution().checkRecord(s))