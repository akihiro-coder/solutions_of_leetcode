import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import src.merge_two_sorted_lists as merge



class Test(unittest.TestCase):
    def test_mergeTwoLists1(self):
        sol = merge.Solution()
        list1, list2= [1,3,4], [1,2,6]
        self.assertEqual(sol.mergeTwoLists(list1, list2), [1,1,2,3,4,6])

    def test_mergeTwoLists2(self):
        sol = merge.Solution()
        list1, list2= [], [1]
        self.assertEqual(sol.mergeTwoLists(list1, list2), [1])


    def test_mergeTwoLists3(self):
        sol = merge.Solution()
        list1, list2= [], []
        self.assertEqual(sol.mergeTwoLists(list1, list2), [])


if __name__ == "__main__":
    unittest.main()



