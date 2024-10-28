  return (n * (n + 1)) / 2;
};

sumToN(30); // 465
sumToN(100); // 5050
sumToN(5); // 15
sumToN(10); // 55
sumToN(1); // 1

The sumToN function takes an integer as an argument, and returns the sum of all the integers from 1 to that number (inclusive). It does this by using the formula for the sum of an arithmetic series, which is given by the equation:

sum = (n * (n + 1)) / 2

In this formula, 'n' represents the upper limit of the series (i.e. the number for which we want to find the sum). By multiplying 'n' by 'n + 1' and dividing the result by 2, we can calculate the sum of all the integers from 1 to 'n'.

For example, if we call sumToN(30), the function will calculate 30 * (30 + 1) / 2, which equals 465. This is the sum of all the integers from 1 to 30, inclusive.

Similarly, if we call sumToN(100), the function will calculate 100 * (100 + 1) / 2, which equals 5050. This is the sum of all the integers from 1 to 100, inclusive.

Overall, the sumToN function provides a simple and efficient way to calculate the sum of a range of integers, using the formula for the sum of an arithmetic series.

*/

The sumToN function is a function that takes an integer as an argument and returns the sum of all the integers from 1 to that number (inclusive). It uses the formula for the sum of an arithmetic series, which is given by the equation:

sum = (n * (n + 1)) / 2

In this formula, 'n' represents the upper limit of the series (i.e. the number for which we want to find the sum). By multiplying 'n' by 'n + 1' and dividing