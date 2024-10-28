  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);
    const sumB = b.toString().split('').reduce((acc, cur)=>  acc + Math.abs(parseInt(cur)), 0);

    if (sumA !== sumB) return sumA - sumB;
    return nums.indexOf(a) - nums.indexOf(b);
  });
}

module.exports = orderByPoints;

/*
  The function `orderByPoints` works by using the `Array.prototype.sort()` method,
  which sorts the elements of an array in place and returns the array.

  The sort order can be either alphabetic (for strings) or numerical (for numbers).
  The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

  In this case, we provide a compare function `(a, b)` which defines the sort order.

  The compare function works by first calculating the sum of the absolute values of the digits of `a` and `b`.

  If the sums are not equal, it returns the difference between the sums. This will sort the numbers based on the sum of their digits in ascending order.

  If the sums are equal, it returns the difference between the indices of `a` and `b` in the original list. This will ensure that if two numbers have the same sum of digits, they are ordered based on their index in the original list.

  Finally, the function returns the sorted array.
  */


/*
  The function `orderByPoints` works by using the `Array.prototype.sort()` method,
  which sorts the elements of an array in place and returns the array.

  The sort order can be either alphabetic (for strings) or numerical (for numbers).
  The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

  In this case, we provide a compare function `(a, b)` which defines the sort order.
