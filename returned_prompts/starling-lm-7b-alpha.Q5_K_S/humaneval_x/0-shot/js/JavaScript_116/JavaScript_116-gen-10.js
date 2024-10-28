  return arr.sort((a, b) => {
    const oneCountA = countOnes(a);
    const oneCountB = countOnes(b);

    if (oneCountA < oneCountB) {
      return -1;
    } else if (oneCountA > oneCountB) {
      return 1;
    } else {
      return a - b;
    }
  });
};

function countOnes(num) {
  return num.toString(2).split('').filter(x => x === '1').length;
}

*/

This solution works by sorting the array using the `sort` method and a compare function. The compare function first counts the number of ones in the binary representation of `a` and `b` using the `countOnes` helper function. If the number of ones in `a` is less than the number of ones in `b`, it returns `-1` to sort `a` before `b`. If the number of ones in `a` is greater than the number of ones in `b`, it returns `1` to sort `a` after `b`. If the number of ones in `a` and `b` are equal, it returns the difference between `a` and `b` to sort `a` before `b` if `a` is smaller than `b`, and vice versa.

The `countOnes` function converts the number to a binary string using `toString(2)` and splits it into an array of characters. It then filters the array to only include characters that are equal to '1' and returns the length of the resulting array, which is the number of ones in the binary representation of the number.

Overall, this solution sorts the array according to the number of ones in the binary representation of each number, and in case of equal number of ones, sorts them based on their decimal values.

*/

/*
In this Kata, you have to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. For similar number of ones, sort based on decimal value.

It must be implemented like this:

>>> sortArray([1, 5, 2, 3, 4]) == [1, 2, 