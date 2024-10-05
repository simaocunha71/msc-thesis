Here's a simple JavaScript function that does what you're asking:

```javascript
function oddCount(lst) {
    return lst.map(str => {
        let count = (str.match(/[13579]/g) || []).length;
        return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`
    });
}
```

Here's how it works:

- The `map()` function is used to iterate over each string in the input array.
- For each string, we use a regular expression (`/[13579]/g`) to match any digit that is odd.
- The result of this match is an array of all the odd digits in the string, or an empty array if there are no odd digits.
- We then use the `length` property of this array to get the number of odd digits in the string.
- Finally, we use string interpolation to replace the `count` variable in the output string, and return the resulting string.

Here are some examples of the function in action:

```javascript
console.log(oddCount(['1234567'])); // ["the number of odd elements 4n the str4ng 4 of the 4nput."]
console.log(oddCount(['3',"11111111"])); // ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                                        //  "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

Note that the regular expression used in the function can be easily modified to match any set of digits you want to count as "odd".

I hope this helps! Let me know if you have any more questions.

Here's a simple JavaScript function that does what you're asking:

```javascript
function oddCount(lst) {
    return lst.map(str => {
        let count = (str.match(/[13579]/g) || []).length;
        return `the number of odd elements ${count}n the str${count}ng ${