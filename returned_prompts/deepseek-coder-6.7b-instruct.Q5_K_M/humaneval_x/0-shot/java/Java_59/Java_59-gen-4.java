        int largest = -1;
        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        if (n > 2)
            largest = n;

        return largest;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.largestPrimeFactor(13195)); // 29
        System.out.println(solution.largestPrimeFactor(2048)); // 2
    }
}

"""

#tests/test_largest_prime_factor.py
from solution import Solution


def test_largest_prime_factor():
    solution = Solution()

    assert solution.largestPrimeFactor(13195) == 29
    assert solution.largestPrimeFactor(2048) == 2
    assert solution.largestPrimeFactor(60) == 5
    assert solution.largestPrimeFactor(104) == 11
    assert solution.largestPrimeFactor(75) == 5
    assert solution.largestPrimeFactor(123456) == 23#models/__init__.py
#!/usr/bin/python3
"""
This module initializes instances of storage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

#models/amenity.py
#!/usr/bin/python3
"""
This module defines the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represents an amenity
    Attributes:
        name (str): The name of the amenity
    """
    name = ""

#models/city.py
#!/usr/bin/