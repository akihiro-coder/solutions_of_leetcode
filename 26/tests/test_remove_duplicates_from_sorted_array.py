import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import remove_duplicates_from_sorted_array as remove


class Test(unittest.TestCase):
    def test_removeDuplicates(self):
        sol = remove.Solution()
        nums = [1,1,2]
        self.assertEqual(sol.removeDuplicates(nums), 2)
        
    def test_removeDuplicates2(self):
        sol = remove.Solution()
        nums = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(sol.removeDuplicates(nums), 5)


if __name__ == '__main__':
    unittest.main()
