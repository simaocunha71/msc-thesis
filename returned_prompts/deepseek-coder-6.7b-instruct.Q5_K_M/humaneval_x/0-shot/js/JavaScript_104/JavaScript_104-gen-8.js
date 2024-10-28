  const noEvenDigits = x.filter(n => {
    const digits = String(n).split('');
    return digits.every(d => parseInt(d) % 2 !== 0);
  });

  return noEvenDigits.sort((a, b) => a - b);
};

console.log(uniqueDigits([15, 33, 1422, 1]));
console.log(uniqueDigits([152, 323, 1422, 10]));
```

This solution works by filtering the given list `x` and checking each number `n` if it contains an even digit. If it contains an even digit, `n` is not added to the resulting list `noEvenDigits`. After filtering, the list is sorted in ascending order and returned.

This solution uses JavaScript's array `filter` method to create a new list that only includes numbers without even digits. It then sorts this new list and returns it.

It uses JavaScript's array `sort` method to sort the list in ascending order. This method sorts the elements of an array in place and returns the array. The default sort order is string Unicode code point order. However, since we want to sort the numbers in ascending order, a comparison function `(a, b) => a - b` is passed to it.

It uses the JavaScript's `every` method to check if all elements in the array pass the test implemented by the provided function. The `parseInt(d) % 2 !== 0` checks if the digit `d` is an odd number. If all digits are odd, it returns `true`, otherwise it returns `false`.

It uses the JavaScript's `split` method to split a string into an array of substrings. It splits the given string `n` at each digit and returns the array of digits.

It uses the JavaScript's `String` method to convert a number into a string.

It uses the JavaScript's `parseInt` function to convert a string into a number.
```
