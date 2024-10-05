```
const filterIntegers = (values) => values.filter(x => typeof x === 'number' && !isNaN(x) && Math.floor(x) === x);
```


Explanation:

*   The `filter()` function is used to create a new array with all elements that pass the test implemented by the provided function.
*   The provided function checks if each element is an integer by using the following conditions:
    *   `typeof x === 'number'`: checks if the element is a number (not a string or boolean).
    *   `!isNaN(x)`: checks if the number is not NaN (Not a Number).
    *   `Math.floor(x) === x`: checks if the number is an integer (i.e., its decimal part is 0).
*   The `filterIntegers` function returns a new array containing only the integers from the original array.