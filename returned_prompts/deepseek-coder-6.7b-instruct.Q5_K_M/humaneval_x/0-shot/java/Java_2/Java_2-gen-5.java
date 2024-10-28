        double truncatedNumber = number - (int)number;
        return truncatedNumber;
    }
}

The function truncateNumber() is taking a double number as input and subtracting the integer part of that number from the original number. The result is the decimal part of the number.
*/



import java.util.*;
import java.lang.*;

class Solution  {
    
    public double truncateNumber(double number) {
        double truncatedNumber = number - (int)number;
        return truncatedNumber;
    }

    public static void main (String[] args)  {
        Solution s = new Solution();
        System.out.println(s.truncateNumber(3.5));
    }
}

// Expected output:
// 0.5

// Given solution is correct and will output the decimal part of the given number.
```


### Python
```python
# Python Solution

class Solution:
    @staticmethod
    def truncate_number(number):
        """
        Given a positive floating point number, it can be decomposed into
        and integer part  (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number.
        >>> truncate_number(3.5)
        0.5
        """
        return number - int(number)

# Testing the function
print(Solution.truncate_number(3.5))

# Expected output:
# 0.5

# Given solution is correct and will output the decimal part of the given number.
```


## Test Cases

```python
# Test cases to validate the solution
assert Solution.truncate_number(3.5) == 0.5
assert Solution.truncate_number(4.2) == 0.2
assert Solution.truncate_number(0.123456) == 0.123456
```


## Performance

The time complexity of this solution is O(1), which means it will take the same amount of time regardless of the size of the input. The