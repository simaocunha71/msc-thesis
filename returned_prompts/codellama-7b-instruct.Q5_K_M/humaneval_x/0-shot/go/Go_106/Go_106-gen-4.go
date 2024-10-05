 
// Factorial
// Factorial of n is n * (n - 1) * (n - 2) * ... * 1
// For example, factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
 
// sum of numbers from 1 to n
// for example, sum of numbers from 1 to 5 is 1 + 2 + 3 + 4 + 5 = 15
 
// for each even number i, the value of the element at index i is the factorial of i
// for each odd number i, the value of the element at index i is the sum of numbers from 1 to i
 
// return a list of size n, such that the value of the element at index i is the factorial of i if i is even
// or the sum of numbers from 1 to i otherwise.
// i starts from 1.
 
// the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
 
// Example:
// F(5) == [1, 2, 6, 24, 15]
 
// F(3) == [1, 2, 6]
 
// F(1) == [1]
 
// F(2) == [1, 2]
 
// F(4) == [1, 2, 6, 24]
 
// F(6) == [1, 2, 6, 24, 120, 720]
 
// F(7) == [1, 2, 6, 24, 120, 720, 5040]
 
// F(8) == [1, 2, 6, 24, 120, 720, 5040, 40320]
 
// F(9) == [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
 
// F