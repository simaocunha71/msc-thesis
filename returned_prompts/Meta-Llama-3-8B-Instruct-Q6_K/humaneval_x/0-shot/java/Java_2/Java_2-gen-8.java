    return number - (int)number; // return the decimal part of the number
} // end of class Solution
```

The above program will return the decimal part of the given number. For instance, if you give the number 3.5, the output will be 0.5.

Explanation:

The given number can be decomposed into two parts: the integer part and the decimal part. The integer part is the largest integer smaller than the given number, and the decimal part is the leftover part always smaller than 1.

The decimal part can be calculated by subtracting the integer part from the given number. In Java, the `int` data type can be used to get the integer part of the number. The `int` data type truncates the decimal part, so subtracting the integer part from the number effectively gives the decimal part.

In the above code, `(int)number` is used to get the integer part of the number, and then the decimal part is calculated by subtracting the integer part from the number. The result is the decimal part of the number.