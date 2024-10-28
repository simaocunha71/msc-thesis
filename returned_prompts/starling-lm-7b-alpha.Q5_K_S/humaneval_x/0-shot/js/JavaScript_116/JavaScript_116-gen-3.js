  const sortByOnes = (a, b) => {
    const onesA = (a + '').match(/1/g).length;
    const onesB = (b + '').match(/1/g).length;
    return onesA - onesB || a - b;
  };

  return arr.sort(sortByOnes);
};

*/

This code defines a function called `sortArray` which takes an array of non-negative integers as input and sorts them based on the number of ones in their binary representation in ascending order.

The function uses another function called `sortByOnes` to compare two numbers in the array and determine the sorting order. The `sortByOnes` function converts each number to a string, counts the number of occurrences of '1' in the binary representation using the `match` method with a regular expression, and returns the difference between the counts. If the counts are equal, it returns the difference between the original numbers.

The `sortArray` function uses the `sort` method on the input array and passes the `sortByOnes` function as the comparison function to perform the sorting. The sorted array is then returned.

The code includes three example test cases to demonstrate the correctness of the `sortArray` function.

Overall, this code provides a solution to the problem of sorting an array of non-negative integers based on the number of ones in their binary representation in ascending order.

*/

