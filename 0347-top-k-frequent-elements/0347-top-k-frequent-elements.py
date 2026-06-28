from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time complexity: 최대 O(N Log N)
        # 자주 반복되는 요소 K개 나열하기
        # 자료구조 -> counter

        nc = Counter(nums)
        top_k_keys = [key for key, count in nc.most_common(k)] # 리스트 컴프리헨션
        return top_k_keys