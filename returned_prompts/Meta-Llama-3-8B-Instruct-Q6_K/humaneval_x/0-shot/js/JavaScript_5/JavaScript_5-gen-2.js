```
const intersperse = (numbers, delimeter) => {
  if (!numbers.length) return [];
  const result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(delimeter);
    result.push(numbers[i]);
  }
  return result;
};
```


Explanation:
The function `intersperse` takes a list of numbers and a delimiter as input. It returns a new list where the delimiter is inserted between every two consecutive elements of the input list.

The function first checks if the input list is empty. If it is, it returns an empty list.

If the list is not empty, it creates a new list `result` and adds the first element of the input list to it.

Then, it iterates over the rest of the input list. For each element, it adds the delimiter to the `result` list, followed by the current element.

Finally, it returns the `result` list.