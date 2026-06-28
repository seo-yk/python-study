class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time complexity: O(N)

        # 2회 이상 보이면 return
        # 1. set을 통해 중복 제거 후 길이 비교

        return len(nums) != len(set(nums))