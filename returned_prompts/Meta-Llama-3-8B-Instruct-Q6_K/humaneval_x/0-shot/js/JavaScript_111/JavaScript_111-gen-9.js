Here is the solution in JavaScript:
```javascript
const histogram = (test) => {
  if (!test) return {};

  const letterCount = {};
  test.split(' ').forEach((letter) => {
    if (letterCount[letter]) {
      letterCount[letter]++;
    } else {
      letterCount[letter] = 1;
    }
  });

  const maxCount = Math.max(...Object.values(letterCount));
  const result = Object.fromEntries(
    Object.entries(letterCount).filter(([letter, count]) => count === maxCount)
  );

  return result;
};
```
Here's an explanation of the solution:

1. We start by splitting the input string into an array of letters using the `split` method with a space character as the separator.
2. We create an object `letterCount` to store the count of each letter.
3. We iterate over the array of letters using `forEach` and update the `letterCount` object accordingly.
4. We find the maximum count using the `Math.max` function and the `Object.values` method.
5. We use the `Object.fromEntries` method to create a new object that only includes the letters with the maximum count.
6. We return the resulting object.

You can test the function with the examples you provided:
```javascript
console.log(histogram('a b c')); // Output: {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')); // Output: {'a': 2, 'b': 2}
console.log(histogram('a b c a b')); // Output: {'a': 2, 'b': 2}
console.log(histogram('b b b b a')); // Output: {'b': 4}
console.log(histogram('')); // Output: {}
```I hope this helps! Let me know if you have any questions.