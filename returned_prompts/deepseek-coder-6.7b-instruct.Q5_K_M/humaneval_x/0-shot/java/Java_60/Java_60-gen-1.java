        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }
}


A: Yes, the time complexity of this function is O(n). This is because there is a single loop that runs from 1 to n. So, the time it takes to run this function grows linearly with the size of the input.

Here is the explanation of the code:

In the function sumToN(int n), a for loop runs from 1 to n. In each iteration, the loop variable i is incremented by 1 and the value of i is added to the variable sum. Finally, the function returns the sum of all numbers from 1 to n.

This solution is simple and efficient, but it's worth mentioning that there is a mathematical formula to calculate the sum of numbers from 1 to n, which can be used to optimize the function. The sum of numbers from 1 to n is given by n*(n+1)/2. However, this formula is more efficient and has a time complexity of O(1), so it's a better solution in terms of efficiency.
*/

// Java program to find sum of all numbers from 1 to n
public class Main
{
    public static int sumToN(int n)
    {
        return n * (n + 1) / 2;
    }
    public static void main(String[] args)
    {
        int n = 5;
        System.out.println(sumToN(n));
    }
}


A: It's correct that the time complexity of this function is O(n). However, note that the time complexity does not actually depend on n, but rather on the number of elements you need to iterate over. In this case, we're iterating over n numbers, so the time complexity is O(n).

A: Here is a more efficient approach using a mathematical formula:

public class Solution {
    public int sumToN(int n) {
        return n * (n + 1) / 2;
    }
}

In this approach, the time complexity is O(1), which is a significant improvement over the original approach. This is because the mathematical formula for the