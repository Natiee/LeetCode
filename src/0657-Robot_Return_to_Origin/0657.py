"""
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。

移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 同样还是count()方法判断字符出现的次数
        l = moves.count('L')
        r = moves.count('R')
        u = moves.count('U')
        d = moves.count('D')
        if l == r and u == d:  # 只有L,R次数相同和 U,D次数相同
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().judgeCircle('UD'))