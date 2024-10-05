Here is the implementation in JavaScript:
```
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) return [];
  const result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(delimeter);
    result.push(numbers[i]);
  }
  return result;
};
```
Explanation:

* If the input list `numbers` is empty, return an empty list.
* Initialize the result list with the first element of `numbers`.
* Loop through the rest of the elements in `numbers`.
* For each element, push the `delimeter` and the element to the result list.
* Return the result list.

This implementation has a time complexity of O(n), where n is the length of the input list `numbers`, and a space complexity of O(n) as well, since we need to store the intermediate result.