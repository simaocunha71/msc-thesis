  return l.filter(x => x > 0);
}

console.log(getPositive([-1, 2, 4, 5, 6])); 
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); 

```

## Filtering Arrays

In this problem, you are given a list of numbers and you have to return only the numbers that meet a certain condition. The condition is that you have to return only positive numbers from the list.

To solve this, you can use the `filter` method in JavaScript. The `filter` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the test is whether the number is greater than 0.

So the solution is to return the result of `l.filter(x => x > 0)`. This will create a new array that only includes the positive numbers from `l`.

## Code Explanation

- The function `getPositive` takes an array `l` as its argument.
- The function returns the result of `l.filter(x => x > 0)`. This uses the `filter` method on `l` to create a new array that includes only the elements from `l` that satisfy the condition `x > 0`.
- The condition `x > 0` is a function that returns `true` if `x` is greater than `0` and `false` otherwise.
- The `filter` method will go through each element `x` in `l` and call this function. If the function returns `true`, `x` is included in the new array. If the function returns `false`, `x` is not included in the new array.
- The new array is then returned as the result of `getPositive`.
- The `console.log` statements at the end of the code call `getPositive` with two different arrays and log the results to the console.

## More Information

- JavaScript's `filter` method is a powerful tool for working with arrays. It can be used to filter arrays based on a condition and create new arrays with only the elements that meet that condition.
