from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        temp = Counter(arr)
        count = 0
        arr = sorted(arr)
        for idx, i in enumerate(arr):
            if idx != len(arr) - 1:
                if arr[idx + 1] ==  arr[idx] + 1:
                    count += temp[i]
        return count