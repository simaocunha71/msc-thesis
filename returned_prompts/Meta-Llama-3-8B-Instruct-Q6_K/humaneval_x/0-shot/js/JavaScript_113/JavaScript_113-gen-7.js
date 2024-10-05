Here is the solution for the problem:

```javascript
const oddCount = (lst) => {
    return lst.map((str, index) => {
        let count = 0;
        for (let char of str) {
            if (parseInt(char) % 2 !== 0) {
                count++;
            }
        }
        return `the number of odd elements ${count}n the str${index+1}ng ${index+1} of the ${index+1}nput.`;
    });
};
```


This solution uses the `map` function to iterate over the input list. For each string, it counts the number of odd digits using a `for` loop and `parseInt` function. The count is then used to create the output string, which is returned as an array.

Note that the `index+1` is used to replace the `i's` with the actual numbers in the output strings. This is because the `map` function uses 0-based indexing, so we need to add 1 to the index to get the correct number.