from typing import List

class Solution:
    def twoSum(self, arr: List[int], target: int) -> int:
        value_index_dict = {}
        for i, value in enumerate(arr):
            x = target - value
            if (x in value_index_dict):
                return [i, value_index_dict[x]]
            value_index_dict[value] = i
        return []
    