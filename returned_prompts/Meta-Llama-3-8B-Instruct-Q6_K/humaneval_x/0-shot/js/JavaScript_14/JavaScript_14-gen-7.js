```
  const prefixes = [];
  for (let i = 1; i <= string.length; i++) {
    prefixes.push(string.slice(0, i));
  }
  return prefixes;
}
```



Explanation:
The function `allPrefixes` takes a string as an argument and returns a list of all its prefixes from shortest to longest. The function uses a `for` loop to iterate over the length of the string, starting from 1 (since the empty string is considered a prefix). For each iteration, it uses the `slice` method to extract the substring from the beginning of the string up to the current index, and adds it to the `prefixes` array. Finally, the function returns the `prefixes` array.

Example:
```
console.log(allPrefixes('abc')); // Output: ['a', 'ab', 'abc']
```



Note: This solution has a time complexity of O(n), where n is the length of the input string, since it iterates over the length of the string once. The space complexity is also O(n), since it stores all the prefixes in an array.