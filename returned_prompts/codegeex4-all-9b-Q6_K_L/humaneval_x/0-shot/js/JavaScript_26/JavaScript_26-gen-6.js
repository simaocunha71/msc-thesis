The following JavaScript function takes a list of integers as input and returns a new list with all duplicate elements removed while maintaining the order of the elements. 

```javascript
const removeDuplicates = (numbers) => {
  let seen = {};
  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!seen[numbers[i]]) {
      seen[numbers[i]] = true;
      result.push(numbers[i]);
    }
  }
  return result;
}
```

This function uses a JavaScript object to keep track of which elements have been seen before. The keys of this object are the elements from the input list, and the values are all set to true. The function then iterates over the input list, and if it encounters an element that has not been seen before (i.e., it is not a key in the seen object), it adds it to the result list and marks it as seen by adding it to the seen object. Finally, it returns the result list.