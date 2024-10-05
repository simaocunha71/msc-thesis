  return values.filter(value => Number.isInteger(value))
}

console.log(filterIntegers(['a', 3.14, 5])) // [5]
console.log(filterIntegers([1, 2, 3, 'abc', {}, []])) // [1, 2, 3]
```


## Answer:

```javascript
const filterIntegers = (values) => {
  return values.filter(value => Number.isInteger(value))
}

console.log(filterIntegers(['a', 3.14, 5])) // [5]
console.log(filterIntegers([1, 2, 3, 'abc', {}, []])) // [1, 2, 3]
```

This solution uses JavaScript's built-in array method `.filter()` to iterate over each element in the `values` array. It checks whether each element is an integer using the `Number.isInteger()` method. If it is, the element is included in the returned array; if not, it is excluded.

The `Number.isInteger()` method checks whether the passed value is an integer. It returns `true` if the value is an integer, and `false` otherwise.

In the example calls, the function filters out all non-integer elements from the arrays and returns a new array with only the integers.
```

## Explanation:

The problem is asking to filter a list of values for integers. 

We can solve this problem by using JavaScript's built-in `.filter()` method. This method creates a new array with all elements that pass the test implemented by the provided function. 

In this case, the function we will pass to `.filter()` will use `Number.isInteger()` to check if each value is an integer. If the value is an integer, it will be included in the new array; otherwise, it will be excluded.

Here is the code:

```javascript
const filterIntegers = (values) => {
  return values.filter(value => Number.isInteger(value))
}

console.log(filterIntegers(['a', 3.14, 5])) // [5]
console.log(filterIntegers