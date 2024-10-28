        if(n <= 1) {
            return n;
        }
        int a = 0;
        int b = 1;
        int c = 0;
        while(n > 2) {
            c = a + b;
            a = b;
            b = c;
            n--;
        }
        return c;
    }
}


    Answer:
    Here's a function that uses an iterative approach to calculate the Fibonacci sequence up to the nth term. The function takes an integer as an argument and returns an integer representing the nth Fibonacci number.

    Here's a step-by-step explanation of the function:

    First, the function checks if the input integer n is less than or equal to 1. If so, it returns n, as the Fibonacci sequence starts with 0 and 1.

    Next, the function initializes three variables: a, b, and c. Variable a is set to 0, variable b is set to 1, and variable c is set to 0. These variables will be used to keep track of the current and next Fibonacci numbers.

    Then, the function enters a while loop that continues until n becomes 2 (since we already handled the base cases). Inside the loop, the function calculates the next Fibonacci number by adding the current Fibonacci number (stored in variable a) and the next Fibonacci number (stored in variable b), and stores the result in variable c.

    After calculating the next Fibonacci number, the function updates the variables: variable a takes the value of variable b, variable b takes the value of variable c, and variable c remains the same.

    Finally, the function decrements the value of n by 1, as we have already calculated the next Fibonacci number. This process continues until n becomes 2.

    Once the while loop finishes, the function returns the value of variable c, which represents the nth Fibonacci number.

    The time complexity of this function is O(n), as it performs n - 2 iterations inside the while loop. The space complexity is O(1), as it only uses a constant amount of extra space to store