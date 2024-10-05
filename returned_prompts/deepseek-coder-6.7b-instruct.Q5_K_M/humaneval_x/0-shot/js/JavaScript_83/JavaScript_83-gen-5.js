  if(n === 1){
    return 2;
  }
  else if(n === 2){
    return 3;
  }
  else{
    return 2 * startsOneEnds(n - 1) + Math.pow(2, n - 2);
  }
}

console.log(startsOneEnds(3));
console.log(startsOneEnds(4));
console.log(startsOneEnds(5));
console.log(startsOneEnds(10));

Explanation:
In this code, we are using a recursive function named "startsOneEnds" that takes a positive integer n as input.

If n equals 1, it returns 2 because there are only two 1-digit numbers that start or end with 1.

If n equals 2, it returns 3 because there are three 2-digit numbers that start or end with 1, namely 11, 12, 21.

Otherwise, it returns 2 times the count of n-1-digit numbers that start or end with 1 plus the count of n-digit numbers that start with 1 and end with any digit plus the count of n-digit numbers that start with any digit and end with 1.

We use the Math.pow function to calculate the count of n-digit numbers that start with 1 and end with 1.

Finally, we call the function with different inputs to demonstrate its functionality.

Please note that the recursion in this solution may cause a stack overflow for larger inputs, in which case you might want to use an iterative solution.
*/

// Time complexity: O(n)
// Space complexity: O(n)

// Note: This solution assumes that the input n is a positive integer.

// Also, note that this solution only counts the numbers that start or end with 1. If you want to count all n-digit numbers that start or end with 1, you would need to add 2 to the result.


// Test Cases
// console.log(startsOneEnds(1)) // 2
// console.log(startsOneEnds(2)) // 3
// console