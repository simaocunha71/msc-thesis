        return x + y;
    }
    
    public static void main(String[] args) {
        // keep this function to test your code
        Solution sol = new Solution();
        System.out.println(sol.add(2, 3)); // should print 5
        System.out.println(sol.add(5, 7)); // should print 12
    }
}

"""


def test_solution():
    assert Solution().add(2, 3) == 5
    assert Solution().add(5, 7) == 12

#test_solution()


# Testing with pytest

def test_add():
    assert Solution().add(2, 3) == 5
    assert Solution().add(5, 7) == 12

#test_add()

def test_add_negative():
    assert Solution().add(-2, 3) == 1
    assert Solution().add(5, -7) == -2
    assert Solution().add(-2, -7) == -9

#test_add_negative()

#pytest.main(["-v", "--tb=line", "test_solution.py"])

#test_solution.py
from test_solution import test_solution, test_add, test_add_negative

test_solution()
test_add()
test_add_negative()

print("All tests passed.")

#pytest.main(["-v", "--tb=line", "test_solution.py"])

#pytest.main(["-v", "--tb=line", "test_solution.py"])

#test_solution_pytest.py
import pytest
from solution import Solution

def test_add():
    assert Solution().add(2, 3) == 5
    assert Solution().add(5, 7) == 12

def test_add_negative():
    assert Solution().add(-2, 3) == 1
    assert Solution().add(5, -7) == -2
    assert Solution().add(-2, -