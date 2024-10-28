
return lst.reduce((accumulator, currentValue, currentIndex) => {
    if (currentIndex % 2 !== 0 && currentValue % 2 === 0) {
        return accumulator + currentValue;
    } else {
        return accumulator;
    }
}, 0);

}

add([4, 2, 6, 7]);



// Output: 2



// Explanation:
// The even elements at odd indices are at lst[1] and lst[3], they are 2 and 7 respectively. 
// So the sum of these elements is 2.


```



## ❓HINT

- You can use the `Array.prototype.reduce()` method to solve this problem.

## 💡 EXPLAINATION

The `reduce` method is a powerful tool that allows you to iterate over an array and accumulate a result. It takes a callback function that is called for each item in the array, and it passes in four arguments:

1. Accumulator: This is the value that is returned by the previous callback invocation or the initial value if supplied. It is the accumulated result.

2. Current Value: This is the current element being processed in the array.

3. Current Index (Optional): This is the index of the current element being processed in the array.

4. Source Array (Optional): This is the array reduce was called upon.

In this problem, you are required to sum up the elements that are at odd indices and are even numbers. Therefore, you need to return the accumulator if the current index is odd and the current value is even, otherwise just return the accumulator as is.

## 👀 TEST CASES

```js
console.log(add([4, 2, 6, 7])); // 2
console.log(add([1, 2, 3, 4, 5])); // 4
console.log(add([10, 20, 30, 40, 50])); // 100
```

## 🏷️ LABELS

#Array #JavaScript