To solve this problem, you can follow these steps:

1. Create an empty array called `result` to store the output strings.
2. Use the `map()` function to iterate over the input `lst` array. For each element in the `lst` array, do the following steps:
   a. Initialize a variable `count` to 0, to keep track of the number of odd digits in the current string.
   b. Iterate over each character in the current string using the `map()` function. For each character, do the following steps:
      i. Convert the character to a number using the `Number()` function.
      ii. Check if the number is odd by using the modulo operator `%` with 2. If the number is odd, increment the `count` variable by 1.
   c. After counting the odd digits, create a string in the format "the number of odd elements Xn the strXng X of the Xnput." by using string concatenation and template literals. Replace X with the count variable.
   d. Push the newly created string into the `result` array using the `push()` function.
3. Return the `result` array after mapping all the strings in the `lst` array.

Here's the code implementation of the solution:

```javascript
const oddCount = (lst) => {
  const result = [];
  lst.map((str) => {
    let count = 0;
    Array.from(str).map((char) => {
      const num = Number(char);
      if (num % 2 !== 0) {
        count += 1;
      }
    });
    result.push(`the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`);
  });
  return result;
};
```

You can test the function with the provided test cases:

```javascript
console.log(oddCount(['1234567']));  // Output: ["the number of odd elements 4n the str4ng 4 of the 4nput."]
console.log(oddCount(['3', "11111111"]));  //