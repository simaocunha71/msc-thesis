```
const filterIntegers = (values) => values.filter(value => typeof value === 'number' && !isNaN(value) && Math.floor(value) === value);
```


The filterIntegers function takes a list of values as an argument. It uses the filter method to create a new array with all elements that pass the test implemented by the provided function.

The provided function checks three conditions:
1. The value must be a number (`typeof value === 'number'`)
2. The value must not be NaN (`!isNaN(value)`)
3. The value must be an integer (i.e., it must be equal to its floor value, `Math.floor(value) === value`)

The function returns a new array containing only the integers from the original list.

For example, when called with the list `[1, 2, 3, 'abc', {}, []]`, the function will return the list `[1, 2, 3]`. When called with the list `['a', 3.14, 5]`, the function will return the list `[5]`.