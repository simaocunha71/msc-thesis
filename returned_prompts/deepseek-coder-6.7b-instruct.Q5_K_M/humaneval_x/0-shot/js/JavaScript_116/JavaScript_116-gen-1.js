  return arr.sort((a, b) => {
    const aBinary = a.toString(2);
    const bBinary = b.toString(2);
    const aOnes = aBinary.split('1').length - 1;
    const bOnes = bBinary.split('1').length - 1;
    return aOnes - bOnes || a - b;
  });
}
*/

sortArray([1, 5, 2, 3, 4])  // [1, 2, 3, 4, 5]
sortArray([-2, -3, -4, -5, -6])  // [-6, -5, -4, -3, -2]
sortArray([1, 0, 2, 3, 4])  // [0, 1, 2, 3, 4]

/*
E:
  In this Kata, you are required to sort an array of non-negative integers in ascending order.
  The integers are sorted based on the number of ones in their binary representation.
  In case of a tie, the decimal value of the number is used for sorting.

  The function takes an array of integers and returns a sorted array.
  The array will only contain non-negative integers.
  The array may be empty.

  The function must be implemented in the following way:
  >>> sortArray([1, 5, 2, 3, 4])  # [1, 2, 3, 4, 5]
  >>> sortArray([-2, -3, -4, -5, -6])  # [-6, -5, -4, -3, -2]
  >>> sortArray([1, 0, 2, 3, 4])  # [0, 1, 2, 3, 4]

  The function must return the sorted array.
  The sorted array must contain the same integers as the input array, but sorted in ascending order.
  The sorted array must be sorted based on the number of ones in the binary representation of the integers.
  In case of a tie, the decimal value of the integers must be used for sorting.
  If the input