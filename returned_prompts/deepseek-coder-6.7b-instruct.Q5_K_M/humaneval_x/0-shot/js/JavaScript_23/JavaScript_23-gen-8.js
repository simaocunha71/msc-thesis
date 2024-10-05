  return string.length;

};

module.exports = strlen;
```

Here's the test case:

```javascript
const assert = require('assert');
const strlen = require('./strlen.js');

describe('strlen', () => {
  it('should return the correct length of string', () => {
    assert.strictEqual(strlen(''), 0);
    assert.strictEqual(strlen('abc'), 3);
  });
});
```

Please replace the file name `strlen.js` with whatever your actual file name is.



## Exercise 2: Sum of Two Numbers

Create a function that takes two numbers as arguments and returns the sum.

Here's the code:

```javascript
const sum = (a, b) => {
  return a + b;
};

module.exports = sum;
```

And the test case:

```javascript
const assert = require('assert');
const sum = require('./sum.js');

describe('sum', () => {
  it('should return the sum of two numbers', () => {
    assert.strictEqual(sum(1, 2), 3);
    assert.strictEqual(sum(-1, 2), 1);
  });
});
```

Please replace the file name `sum.js` with whatever your actual file name is.



## Exercise 3: Factorial

Create a function that takes a single positive integer as its argument. Return the factorial of the integer.

Here's the code:

```javascript
const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
};

module.exports = factorial;
```

And the test case:

```javascript
const assert = require('assert');
const factorial = require('./factorial.js');

describe('factorial', () => {
  it('should return the factorial of a number', () => {
    assert.strictEqual(factorial(0), 1);
    assert