from typing import List

class Solution:
    def twoSum(self, arr: List[int], target: int) -> int:
        value_index_dict = self.__convertListToDict(arr, target)
        print("Inside dictionary = ", value_index_dict)
        resultArray = []
        for i, value in enumerate(arr):
            key = target - value
            value = value_index_dict.get(key)
            print("key = ", key, " value = ", value)
            if (i == value):
                print("same index")
            elif (value):
                resultArray.append(i)
                resultArray.append(value)
                return resultArray
        return resultArray
    
    def __convertListToDict(self, arr: List[int], k: int) -> dict:
        value_index_dict = {}
        for i, value in enumerate(arr):
            value_index_dict[value] = i
        return value_index_dict
    