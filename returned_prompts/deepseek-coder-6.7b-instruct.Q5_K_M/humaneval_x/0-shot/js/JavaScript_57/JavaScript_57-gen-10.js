  return l.length <= 2 ||
    (l.every((e, i) => i === 0 || e > l[i - 1]) || l.every((e, i) => i === 0 || e < l[i - 1]));
}

console.log(monotonic([1, 2, 4, 20])); // true
console.log(monotonic([1, 20, 4, 10])); // false
console.log(monotonic([4, 1, 0, -10])); // true
```

The function `monotonic` checks if the list is either monotonically increasing or decreasing.

First, it checks if the length of the list is less than or equal to 2, as these are the base cases for a monotonic list.

Then, it checks if all elements in the list are greater than the previous one, which would signify a monotonically increasing list. 

If this is not the case, it checks if all elements are less than the previous one, which would mean the list is monotonically decreasing.

If neither of these conditions is met, the function returns `false`, indicating that the list is not monotonically increasing or decreasing.

Finally, the function returns `true` if the list is monotonically increasing or decreasing.

The `every` function is used to check if all elements in the list satisfy the condition. It returns `true` if the condition is satisfied for all elements, and `false` otherwise.

The `console.log` statements are used to test the function with the provided examples.

The `i === 0` condition in the `every` function is used to skip the first element in the list, as it does not have a previous element to compare it with.

The `||` operator is used to check both conditions at the same time. If any of them is `true`, the overall condition will also be `true`.

The `every` function is used twice to check if the list is either monotonically increasing or decreasing. If both conditions are met, the function returns `true`. If not, it returns `false`.

Overall, this function is a succinct way to check if a list is monotonically increasing or decreasing.