  return l.filter(n => n > 0)

}

console.log(getPositive([-1, 2, 4]))
console.log(getPositive([-1, 2, -4, 5, 6]))
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

The function `getPositive` filters the list `l` to only include numbers that are greater than 0. It uses the JavaScript array `filter` method to create a new array with only the positive numbers.

The `filter` function is a higher-order function that takes a callback function and applies it to every element in the array, creating a new array with all the elements for which the callback function returns `true`.

In this case, the callback function is `n => n > 0`, which is an arrow function that takes an element `n` and returns whether `n` is greater than 0.

The `console.log` statements are used to test the function with various inputs.

This solution assumes that the input list `l` will only contain numbers. If this is not the case, you may want to add error handling to account for non-numeric elements in the list.

You can run this code in a JavaScript environment to test it.

Note: The code snippets provided above are written in JavaScript.

---

### 2. JavaScript: Find the Longest Word in a String

```javascript
