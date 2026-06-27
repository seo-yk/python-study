class Solution(object):
    def findTheDifference(self, s, t):
        # time complexity : O(N log N)
        # space complexity : 
        
        # s와 t 다른점 찾기
        # 1. suffling -> sort, 일단 정렬하기
        # 2. 동일한 문자인지 확인
        # 3. 만약 s만큼 다 돌았는데 다른 게 없다면? t의 마지막 letter return
        # 4. 만약 s의 길이가 0이면 t[-1]

        st = sorted(t)
        ss = sorted(s)

        for i in range(len(s)):
            if ss[i] != st[i]:
                return st[i]
        
        return st[-1]