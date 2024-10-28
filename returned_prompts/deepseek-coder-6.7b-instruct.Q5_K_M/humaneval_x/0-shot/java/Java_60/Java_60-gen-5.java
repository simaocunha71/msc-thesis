import java.util.*;
import java.lang.*;

class Solution 
{
    public int sumToN(int n) 
    {
        int sum = 0;
        for (int i = 1; i <= n; i++) 
        {
            sum += i;
        }
        return sum;
    }
}

You can test it using the following code:

public class Main
{
    public static void main(String[] args) 
    {
        Solution sol = new Solution();
        System.out.println(sol.sumToN(30)); // Should print 465
        System.out.println(sol.sumToN(100)); // Should print 5050
        System.out.println(sol.sumToN(5)); // Should print 15
        System.out.println(sol.sumToN(10)); // Should print 55
        System.out.println(sol.sumToN(1)); // Should print 1
    }
}

This code creates an instance of the Solution class, and then calls the sumToN method with different integers to test the function. The results are then printed to the console.

The function sumToN uses a for loop to iterate over all integers from 1 to n (inclusive), adding each one to a running total. When the loop has finished, it returns the total sum.

This is a simple example of a function that computes the sum of all integers from 1 to n, which is a common mathematical operation.

I hope this helps, and let me know if you have any other questions.


A: The function you are asking about is called the sum of arithmetic series. It is a common mathematical operation and can be computed using the formula: n*(n+1)/2

The function sumToN(int n) can be implemented as follows:

```java
public int sumToN(int n) {
    return n * (n + 1) / 2;