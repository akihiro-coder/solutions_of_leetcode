import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import src.remove_element


class Test(unittest.TestCase):
    def test_removeElement1(self):
        sol = src.remove_element.Solution()
        nums = [3,2,2,3]
        val = 3
        self.assertEqual(sol.removeElement(nums, val), 2)

    def test_removeElement2(self):
        sol = src.remove_element.Solution()
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        self.assertEqual(sol.removeElement(nums, val), 5)



if __name__ == "__main__":
    unittest.main()


