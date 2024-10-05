  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = q.join('') === q.reverse().join('');

  return sum <= w && isBalanced;
}

console.log(willItFly([1, 2], 5)) // false
console.log(willItFly([3, 2, 3], 1)) // false
console.log(willItFly([3, 2, 3], 9)) // true
console.log(willItFly([3], 5)) // true

```

## 3. What is a callback function and why is it used?

A callback function is a function that is passed as an argument to another function and is executed after some operations are performed. It is used in JavaScript to maintain the flow of the program and to manage the execution of tasks.

Callbacks are used for several reasons:

1. Asynchronous Programming: Callbacks are used in asynchronous programming to handle the results of an asynchronous operation.
2. Event-Driven Programming: Callbacks are used in event-driven programming to handle events such as user clicks, server responses, etc.
3. Control Flow: Callbacks are used to control the flow of the program. They are used to ensure that certain code is executed after other code.
4. Error Handling: Callbacks are used to handle errors during asynchronous operations.

Here is an example of a callback function:

```javascript
function greet(name, callback) {
    console.log('Hi ' + name);
    callback();
}

greet('John', function() {
    console.log('This is a callback function');
});
```

In this example, `greet` function takes two arguments: `name` and `callback`. The `callback` function is a callback function that is executed after the greeting message is printed.

## 4. What is the difference between null and undefined in JavaScript?

In JavaScript, both `null` and `undefined` represent the absence of a value. However, they are used in different ways:

1. `undefined`: A variable that has been declared but not yet assigned a value is `undefined`.
2. `