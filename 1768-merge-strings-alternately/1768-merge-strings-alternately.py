class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        # time complexity : O(N log N)까지 허용, 풀이: O(N)
        # space complexity : O(N)

        # 1. 두 문자열의 길이를 구하고 더 큰 값 찾기
        # 2. 더 큰 값만큼 루프 돌리기
        # 3. 인덱스가 각 문자열 길이보다 작을 때만 결과 배열에 번갈아 추가
        # 4. 배열을 문자열로 합쳐서 리턴 -> O(N^2)의 메모리 낭비 방지

        result = []

        len1 = len(word1)
        len2 = len(word2)

        max_len = max(len1, len2)

        for i in range(max_len):
            # Prevent IndexOutOfBoundsException
            if i < len1:
                result += word1[i]

            if i < len2:
                result += word2[i]

        return "".join(result)
