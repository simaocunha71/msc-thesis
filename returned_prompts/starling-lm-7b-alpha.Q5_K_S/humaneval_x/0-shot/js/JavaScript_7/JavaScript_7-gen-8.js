Here's a possible solution using Array.filter method:

```javascript
const filterBySubstring = (strings, substring) => {
  return strings.filter(str => str.includes(substring));
};
```

This function takes an array of strings and a substring as arguments. It uses Array.filter method to iterate over the input array and only return strings that include the given substring.

Explanation:
- The function `filterBySubstring` takes two arguments: `strings` (the input array of strings) and `substring` (the substring to filter for).
- Inside the function, `Array.filter` method is used to iterate over each element in the `strings` array.
- The arrow function `(str => str.includes(substring))` is used as the filtering condition. It checks if the current string (`str`) includes the given `substring`. If it does, the string is included in the filtered result, otherwise it is excluded.
- The filtered result is then returned by the function.

By using this function, you can easily filter an array of strings based on whether they contain a specific substring or not.

For example, when you call `filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')`, it will return `['abc', 'bacd', 'array']` as the output, because only these strings include the substring 'a'.

I hope this helps! Let me know if you have any further questions.

Here are some additional resources that you might find helpful:
- [Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [Array.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
- [String.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)

Best,
Andrei

P.S. Make sure to check the "Add solution as an answer" checkbox before submitting a solution, to properly mark it as the correct answer to your question