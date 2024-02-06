import unittest
from src.array_for_maximum_sum import Solution

class two_sum_test(unittest.TestCase):

    def test_0(self):
        result = Solution().twoSum([-3, 4, 3, 90], 0)
        print(result)
        self.assertEqual(result, [0,2])

    def test_1(self): 
        result = Solution().twoSum([3,2,4], 6)
        print(result)
        self.assertEqual([1, 2], result)
    
    def test_2(self): 
        result = Solution().twoSum([0,4,3,0], 0)
        print(result)
        self.assertEqual([0,3], result) 
    
    def test_3(self): 
        result = Solution().twoSum([2,7,11,15,1,5], 9)
        print(result)
        self.assertEqual([0,1], result) 
    
    def test_4(self): 
        result = Solution().twoSum([1,3,4,2], 6)
        print(result)
        self.assertEqual([2,3], result)

if __name__ == '__main__':
    unittest.main()
