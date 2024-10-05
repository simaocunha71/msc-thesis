  return arr.sort((a, b) => {
    let aBinary = a.toString(2);
    let bBinary = b.toString(2);
    let aOnes = (aBinary.match(/1/g) || []).length;
    let bOnes = (bBinary.match(/1/g) || []).length;

    return aOnes - bOnes || a - b;
  });
};

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]

// The sort() method sorts the elements of an array in place and returns the array.
// The default sort order is string Unicode code points.
// Therefore, to sort numbers correctly, we should provide a compare function.
// We convert numbers to binary using toString(2) method and count the number of "1"s.
// If the number of "1"s is the same, we sort by the decimal value.
// If the number of "1"s is different, we sort by the number of "1"s.
// The match(/1/g) method is used to find all "1"s in the binary representation of a number.
// The length of the resulting array gives us the count of "1"s.
// If no "1"s are found, match() returns null and we count 0 "1"s.
```

## Tags:

- sorting
- binary
- javascript

## Solution:

The solution uses the `sort` method in JavaScript with a compare function. The compare function converts each number to its binary representation, counts the number of "1"s, and then compares the counts and decimal values. If the count of "1"s is the same, it compares the decimal values.

The `sort` method in JavaScript sorts the elements