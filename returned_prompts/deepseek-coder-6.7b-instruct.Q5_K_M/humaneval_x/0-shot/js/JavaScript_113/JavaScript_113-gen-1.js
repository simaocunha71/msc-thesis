let result = lst.map(str => {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (parseInt(str[i]) % 2 !== 0) {
            count++;
        }
    }
    return count;
});

return result.map(num => `the number of odd elements ${num}n the str${num}ng ${num} of the ${num}nput.`);
}

console.log(oddCount(['1234567']));
console.log(oddCount(['3',"11111111"]));

// Explanation:
// The function oddCount takes a list of strings as its argument. It maps through the list, and for each string it counts the number of odd digits.
// It then maps through the resultant counts, creating the final strings.
// The count of odd digits is added to the string at the correct place using template strings.
// The final result is a list of strings in the required format.
// The time complexity of this solution is O(n*m) where n is the number of strings and m is the length of the longest string.
// The space complexity is O(n) as we are storing the result in a new array.

*/

module.exports = oddCount;
```

## 2. Create a function that returns the sum of all even numbers from a given list.

```javascript
/*
