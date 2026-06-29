class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """complexity
            - 정렬: O(n log n)
            - 반복문: O(n)
            - nums.length: 최소 O(n log n)
            - sorted() 대신 sort(): 새 배열 대신 원본 배열 정렬 

            문제: 반복 시 return true
            1. nums 배열 제자리 정렬
            2. 0부터 len(nums)-2까지 순회
            3. 현재 값과 다음 값이 같으면 True
            4. 끝까지 없으면 False
        """

        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False