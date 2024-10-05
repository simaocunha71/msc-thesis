  let max = Math.max(...lst);
  let count = new Array(max + 1).fill(0);
  
  for(let i = 0; i < lst.length; i++) {
    count[lst[i]]++;
  }
  
  for(let i = max; i > 0; i--) {
    if(count[i] >= i) return i;
  }
  return -1;
}

// Test cases
console.log(search([4, 1, 2, 2, 3, 1])); // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // 3
console.log(search([5, 5, 4, 4, 4])); // -1

// In the first test, the frequency of 2 is 2 which is greater than 2, so 2 is the answer.
// In the second test, the frequency of 3 is 3 which is greater than 3, so 3 is the answer.
// In the third test, there is no number which has the frequency greater than or equal to its value, so -1 is the answer.

// This code works by first finding the maximum value in the list, then creating an array of zeros of size equal to the maximum value plus one. It then iterates over the list, incrementing the count at each index that matches the value in the list. Finally, it iterates from the maximum value down to 1, returning the first value that has a count that is greater than or equal to its value. If no such value is found, it returns -1.

// The time complexity of this code is O(n), where n is the length of the list, because it iterates over the list twice. The space complexity is also O(n), because it creates an array of size n.

// This code should be able to handle lists of any size and contain any positive integer values.

// Note: This code assumes that the list will only contain positive integers. If there are negative integers in the list, this code will not work as expected.
```


## Code: Python
```python
# Python