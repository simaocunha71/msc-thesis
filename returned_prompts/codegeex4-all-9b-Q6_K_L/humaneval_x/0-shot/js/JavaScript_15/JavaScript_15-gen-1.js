The task is to create a function that generates a string of numbers starting from 0 up to n inclusive, separated by spaces.

Here's how you can do it in JavaScript:

```javascript
const stringSequence = (n) => {
    let result = '';
    for (let i = 0; i <= n; i++) {
        result += i.toString();
        if (i !== n) {
            result += ' ';
        }
    }
    return result;
};
```

This function starts by initializing an empty string `result`. It then iterates from 0 to n (inclusive), converting each number to a string and appending it to `result`. A space is added after each number except the last one.

You can test the function with the provided test cases:

```javascript
console.log(stringSequence(0)); // '0'
console.log(stringSequence(5)); // '0 1 2 3 4 5'
```