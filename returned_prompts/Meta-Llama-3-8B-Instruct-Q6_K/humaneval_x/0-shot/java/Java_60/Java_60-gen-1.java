        int sum = 0;
        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
S:

In this function, we are using a for loop to iterate through the numbers from 1 to n. For each iteration, we are adding the current number to the sum. The loop continues until we have added all the numbers from 1 to n to the sum. Finally, we return the sum.

For example, if we call `sumToN(5)`, the function will add 1 + 2 + 3 + 4 + 5 = 15. If we call `sumToN(10)`, the function will add 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55. If we call `sumToN(1)`, the function will simply return 1. If we call `sumToN(100)`, the function will add all the numbers from 1 to 100, which is a total of 5050. This function can be used to calculate the sum of any sequence of numbers.