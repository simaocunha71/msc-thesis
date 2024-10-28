Here is a JavaScript function that sorts an array of non-negative integers according to the number of ones in their binary representation in ascending order, and for similar number of ones, sorts based on decimal value:

```javascript
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const countA = (a.toString(2)).replace(/0/g, '').length;
    const countB = (b.toString(2)).replace(/0/g, '').length;
    if (countA === countB) {
      return a - b;
    }
    return countA - countB;
  });
};
```

This function uses the built-in `sort` method of the array, which sorts the array in place. The `sort` method takes a compare function as its second argument. This compare function is called for each pair of elements in the array, and it returns a negative value if the first element is smaller, a positive value if the first element is larger, and 0 if the elements are equal.

In this case, the compare function calculates the number of ones in the binary representation of each element by converting the element to a string in base 2 (using the `toString(2)` method), replacing all the zeros with an empty string (using the `replace(/0/g, '')` method), and then getting the length of the resulting string (using the `length` property).

If the number of ones in the binary representation of the two elements is equal, the compare function returns the difference between the two elements (using the `-` operator). This causes the `sort` method to sort the elements based on their decimal value.

If the number of ones in the binary representation of the two elements is not equal, the compare function returns the difference between the two counts (using the `-` operator). This causes the `sort` method to sort the elements based on the number of ones in their binary representation.