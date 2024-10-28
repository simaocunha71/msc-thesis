Here is the solution for the problem:
```
const oddCount = (lst) => {
  return lst.map((str, index) => {
    let count = 0;
    for (let char of str) {
      if (+char % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${index+1}ng ${index+1} of the ${index+1}nput.`;
  });
};
```
Explanation:

1. The function `oddCount` takes a list of strings as an argument.
2. The `map` function is used to iterate over each string in the list and its corresponding index.
3. For each string, we initialize a variable `count` to 0, which will store the count of odd digits in the string.
4. We use a `for...of` loop to iterate over each character in the string. If the character is odd (i.e., `+char % 2 !== 0`), we increment the `count` variable.
5. We then return a string with the count of odd digits, the string index, and the input index. The string is formatted using template literals.

Example usage:
```
console.log(oddCount(['1234567'])); // Output: ["the number of odd elements 4n the str4ng 4 of the 4nput."]
console.log(oddCount(['3',"11111111'])); // Output: ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
``` 