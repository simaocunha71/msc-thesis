You can solve this problem with the help of a simple loop. Here is a JavaScript solution:

```javascript
const howManyTimes = (string, substring) => {
    let count = 0;
    for(let i = 0; i < string.length; i++) {
        if(string.substring(i, i + substring.length) === substring) {
            count++;
        }
    }
    return count;
}
```

This function will iterate through the string and check if the substring starting from the current index matches the target substring. If it does, it increments the count. At the end, it returns the total count.

You can test the function with the following code:

```javascript
console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3
```

This should give you the expected output.