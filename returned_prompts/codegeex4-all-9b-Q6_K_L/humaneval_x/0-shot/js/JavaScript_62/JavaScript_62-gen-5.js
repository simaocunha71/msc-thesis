```java
const derivative = (xs) => {
  // check if xs is an array
  if (!Array.isArray(xs)) {
    throw new Error('Input must be an array');
  }
  // check if xs is empty
  if (xs.length === 0) {
    throw new Error('Input array must not be empty');
  }
  // check if xs contains only numbers
  for (let i = 0; i < xs.length; i++) {
    if (typeof xs[i] !== 'number') {
      throw new Error('Input array must only contain numbers');
    }
  }
  // calculate derivative
  const derivative = [];
  for (let i = 1; i < xs.length; i++) {
    derivative.push(xs[i] * i);
  }
  return derivative;
}
```
