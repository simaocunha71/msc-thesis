Here is a solution for the problem:

```javascript
const rollingMax = (numbers) => {
  if (!numbers || numbers.length === 0) {
    return [];
  }
  const result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(Math.max(result[i-1], numbers[i]));
  }
  return result;
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]
```


Explanation:

1. First, we check if the input list is empty or null. If it is, we return an empty list.

2. We then initialize an empty list `result` and add the first element of the input list to it.

3. We loop through the input list starting from the second element (index 1).

4. For each element, we calculate the maximum between the current element and the previous maximum (which is stored in the `result` list at the current index minus one).

5. We add the calculated maximum to the `result` list.

6. Finally, we return the `result` list, which contains the rolling maximum for each element in the input list.

This solution has a time complexity of O(n), where n is the length of the input list, because we only need to iterate through the list once. The space complexity is O(n) as well, because we need to store the result list.