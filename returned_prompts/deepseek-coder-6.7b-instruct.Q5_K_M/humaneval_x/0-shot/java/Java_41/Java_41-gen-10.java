        return (n * (n - 1)) / 2;
    }

}

The answer is (n * (n - 1)) / 2 because each car will collide with n-1 other cars. So for n cars, there are n*(n-1)/2 collisions.

The problem can be solved with the concept of combinations. The total number of pairs of cars is n * (n - 1) and each pair can be considered a collision. So, the total number of collisions is n * (n - 1) / 2.

Time complexity: O(1)
Space complexity: O(1)
*/

// JAVA Solution
// Time complexity: O(1)
// Space complexity: O(1)
class Solution {
    public int carRaceCollision(int n) {
        return (n * (n - 1)) / 2;
    }
}

// Python Solution
class Solution:
    def carRaceCollision(self, n: int) -> int:
        return (n * (n - 1)) // 2

// C++ Solution
class Solution {
public:
    int carRaceCollision(int n) {
        return n * (n - 1) / 2;
    }
};
```

## Test Cases

```python
assert Solution().carRaceCollision(3) == 3
assert Solution().carRaceCollision(4) == 6
```

## Constraints

- 1 <= n <= 10^9

## Note

This problem can be solved by using the concept of combinations. The total number of pairs of cars is n * (n - 1) and each pair can be considered a collision. So, the total number of collisions is n * (n - 1) / 2.

This problem can also be solved by using the mathematical formula for the sum of the first n integers. The sum of the first n integers is n * (n + 1) / 2. Since each car is paired with n - 1 other cars, the total number of collisions is n * (n + 1) / 2 - n = (n * (n - 1)) / 