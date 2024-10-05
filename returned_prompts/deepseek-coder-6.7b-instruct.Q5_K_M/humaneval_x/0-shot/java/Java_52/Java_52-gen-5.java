        for(int num : l){
            if(num >= t){
                return false;
            }
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.belowThreshold(Arrays.asList(1, 2, 4, 10), 100)); // should print true
        System.out.println(solution.belowThreshold(Arrays.asList(1, 20, 4, 10), 5)); // should print false
    }
}

"""

    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.belowThreshold([1, 2, 4, 10], 100), True)
        self.assertEqual(solution.belowThreshold([1, 20, 4, 10], 5), False)


if __name__ == '__main__':
    unittest.main()


"""


import unittest

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.belowThreshold([1, 2, 4, 10], 100), True)
        self.assertEqual(solution.belowThreshold([1, 20, 4, 10], 5), False)


if __name__ == '__main__':
    unittest.main()

"""

#Python-test/test_solution.py
import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.belowThreshold([1, 2, 4, 10], 100), True)
        self.assertEqual(solution.belowThreshold([1, 20, 4, 10], 5), False)


if __name__ == '