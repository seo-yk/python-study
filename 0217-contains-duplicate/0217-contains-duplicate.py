class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time complexity: O(N Log N)

        # 2회 이상 보이면 return
        # 1. nums 정렬
        # 2. 루프를 통해 이전 값과 다음 값이 동일한지 비교 -> prevent IndexOutOfBounds range(n-1)까지

        sn = sorted(nums)
        for i in range(len(sn)-1):
            if sn[i] == sn[i+1]:
                return True

        return False