  const sortByOnesInBinary = (a, b) => {
    const binReprA = a.toString(2);
    const binReprB = b.toString(2);
    const onesA = binReprA.match(/1/g) || [];
    const onesB = binReprB.match(/1/g) || [];

    if (onesA.length !== onesB.length) {
      return onesA.length - onesB.length;
    }

    return a - b;
  };

  return arr.sort(sortByOnesInBinary);
};

*/

In this Kata, you have to sort an array of non-negative integers according to
  number of ones in their binary representation in ascending order.
  For similar number of ones, sort based on decimal value.

  It must be implemented like this:
  >>> sortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
  >>> sortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
  >>> sortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]

Here's a solution to the problem using javascript:

function sortArray(arr) {
  return arr.sort((a, b) => {
    const binReprA = a.toString(2);
    const binReprB = b.toString(2);
    const onesA = binReprA.match(/1/g) || [];
    const onesB = binReprB.match(/1/g) || [];

    if (onesA.length !== onesB.length) {
      return onesA.length - onesB.length;
    }

    return a - b;
  });
}

To test the function, you can use the following test cases:

console.log(sortArray([1, 5, 2, 3, 4]) === [1, 2, 3, 4, 