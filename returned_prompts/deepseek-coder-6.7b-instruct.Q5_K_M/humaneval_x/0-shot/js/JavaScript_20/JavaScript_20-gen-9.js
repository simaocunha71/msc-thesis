  numbers.sort((a, b) => a - b);

  let smallestDifference = Infinity;
  let closestElements;

  for(let i = 0; i < numbers.length - 1; i++) {
    const difference = numbers[i + 1] - numbers[i];

    if(difference < smallestDifference) {
      smallestDifference = difference;
      closestElements = [numbers[i], numbers[i + 1]];
    }
  }

  return closestElements;
}

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)
```

## Answer:

```javascript
