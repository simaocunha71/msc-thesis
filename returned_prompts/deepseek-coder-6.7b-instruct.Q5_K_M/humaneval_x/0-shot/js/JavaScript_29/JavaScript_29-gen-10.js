  return strings.filter(str => str.startsWith(prefix));

};

console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'b')); // ['bcd']
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'c')); // ['cde']
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'ar')); // ['array']
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'z')); // []
console.log(filterByPrefix([], 'a')); // []

// This solution uses the Array.prototype.filter() method to iterate over each string in the array.
// The callback function checks if each string starts with the provided prefix.
// If it does, the string is included in the final array. If not, it is excluded.

// This solution has a time complexity of O(n), where n is the number of strings in the input array.
// This is because the filter method traverses the array once.

// This solution has a space complexity of O(n), where n is the number of strings in the input array,
// because in the worst case, every string might be selected to be included in the final array.

// In summary, this solution is efficient and easy to understand.
```

## 4. Find the longest string in an array

```javascript
