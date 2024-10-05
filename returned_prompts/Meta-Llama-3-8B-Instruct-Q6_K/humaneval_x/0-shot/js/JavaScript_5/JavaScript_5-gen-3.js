```
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) {
    return [];
  }
  return [numbers[0]].concat(Array(numbers.length - 1).fill(delimeter).map(() => delimeter)).concat(numbers.slice(1));
};
```


Explanation:
The function takes two parameters, `numbers` and `delimeter`. It returns a new list where `delimeter` is inserted between every two consecutive elements of the input list `numbers`.

If the input list `numbers` is empty, the function returns an empty list.

The function uses the `concat` method to concatenate the first element of `numbers` with an array of `delimeter` repeated `numbers.length - 1` times. This effectively inserts `delimeter` between every two consecutive elements of `numbers`. The `map` method is used to create an array of `delimeter` with the same length as `numbers.length - 1`. The `slice(1)` method is used to get all elements of `numbers` except the first one.

Here is the breakdown of the function:

* `[numbers[0]]`: gets the first element of `numbers` and wraps it in an array.
* `Array(numbers.length - 1).fill(delimeter)`: creates an array of `delimeter` with the same length as `numbers.length - 1`.
* `map(() => delimeter)`: maps the array of `delimeter` to an array of `delimeter` with the same length.
* `concat(numbers.slice(1))`: concatenates the array of `delimeter` with the rest of the elements of `numbers` (except the first one).

The function returns the resulting array with `delimeter` inserted between every two consecutive elements of `numbers`.