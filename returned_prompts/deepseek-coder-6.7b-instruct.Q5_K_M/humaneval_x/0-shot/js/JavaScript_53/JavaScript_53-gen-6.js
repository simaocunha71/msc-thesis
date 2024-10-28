  return x + y;
}

const result = add(2, 3);
console.log(result); // 5

const result2 = add(5, 7);
console.log(result2); // 12

// or simply

const add = (x, y) => x + y;
console.log(add(2, 3)); // 5
console.log(add(5, 7)); // 12
```

### Arrow function and this keyword

Arrow functions do not have their own `this`. The `this` value inside an arrow function is the same as the `this` value outside the arrow function.

```javascript
// inside arrow function, this does not bind to anything
const obj = {
  id: 42,
  coolFunc: () => {
    console.log(this.id);  // undefined
  }
};

obj.coolFunc();  // outputs: undefined
```

In the example above, `this.id` inside `coolFunc` is `undefined` because arrow functions do not have their own `this` and `obj.coolFunc` does not create a new scope, so the `this` inside `coolFunc` is the same as `this` outside of `coolFunc`.

### Arrow function and `arguments` keyword

Arrow functions do not have their own `arguments` variable. Instead, they inherit it from the parent scope.

```javascript
// inside arrow function, arguments does not bind to anything
const obj = {
  coolFunc: () => {
    console.log(arguments);
  }
};

obj.coolFunc();  // TypeError: arguments is not defined
```

In the example above, `arguments` inside `coolFunc` is `undefined` because arrow functions do not have their own `arguments` and `obj.coolFunc` does not create a new scope, so the `arguments` inside `coolFunc` is the same as `arguments` outside of `coolFunc`.

### Arrow function and `super` keyword

Arrow functions do not have their own `super`. The `super` keyword inside an arrow function refers to the `super` in the parent scope.