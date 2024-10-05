result := make([]int, 0)

	for _, value := range values {
		if val, ok := value.(int); ok {
			result = append(result, val)
		}
	}

	return result
}

```

## Output

```
[5]
[1, 2, 3]
```

## Explanation

The function `FilterIntegers()` takes in a slice of empty interface as argument. It iterates over each value in the slice. If the value is of type `int`, it appends it to the `result` slice. At the end of the function, it returns the `result` slice which contains only the integers from the input slice.

In the second example, it also filters out non-integer values like `'abc'`, `{}` and `[]` as they are not of type `int`.

## Time complexity

The time complexity of the function is O(n), where n is the number of elements in the input list. This is because it needs to iterate over each element in the list once.

## Space complexity

The space complexity of the function is O(k), where k is the number of integers in the input list. This is because it creates a new slice to store the integers.

## Constraints

- The input list can contain any type of value, including integers, floats, strings, etc.
- The function should return a list of integers only.

## Test cases

- `FilterIntegers(['a', 3.14, 5])` returns `[5]`
- `FilterIntegers([1, 2, 3, 'abc', {}, []])` returns `[1, 2, 3]`
- `FilterIntegers([10, '20', 30.5, '40.5', 'abc', {}, []])` returns `[10]`
- `FilterIntegers([])` returns `[]`
- `FilterIntegers(['10', '20', '30', '40'])` returns `[]`
- `FilterIntegers([1, 2.2, 3.3, 4.4, 5])` returns `[1,