To solve this problem, you can follow these steps:

1. Split the input string into an array of words using the `split()` method.
2. Create an empty string to store the result.
3. Loop through each word in the array.
4. For each word, convert it into an array of characters using the `split()` method.
5. Sort the array of characters in ascending order based on their ASCII value using the `sort()` method.
6. Join the sorted array of characters back into a string using the `join()` method.
7. Append the sorted word to the result string.
8. Return the result string.

Here's the implementation of the `antiShuffle()` function:

```javascript
const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    return word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }).join(' ');
};
```

Let's test the function with the provided examples:

```javascript
console.log(antiShuffle('Hi')); // Output: 'Hi'
console.log(antiShuffle('hello')); // Output: 'ehllo'
console.log(antiShuffle('Hello World!!!')); // Output: 'Hello !!!Wdlor'
```

The output of the above code will be:

```
Hi
ehllo
Hello !!!Wdlor
```