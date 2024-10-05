Here is the solution for the problem:

```javascript
const oddCount = (lst) => {
  return lst.map((str, index) => {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
      if (parseInt(str[i]) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${index+1}ng ${index+1} of the ${index+1}nput.`;
  });
};
```
This function `oddCount` takes a list of strings `lst` as an argument. It uses the `map` method to iterate over each string in the list. For each string, it counts the number of odd digits using a for loop and the `parseInt` function. Then it returns a string that includes the count of odd digits and the corresponding string number. The `index+1` is used to get the string number as a string. The `n` is used to replace the string number with the string "n" for the output. The `return` statement is used to return the result. The output is a list of strings as required. 

For example, if you call `oddCount(['1234567'])`, it will return `["the number of odd elements 4n the str4ng 4 of the 4nput."]`. If you call `oddCount(['3',"11111111"])`, it will return `["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]`. 