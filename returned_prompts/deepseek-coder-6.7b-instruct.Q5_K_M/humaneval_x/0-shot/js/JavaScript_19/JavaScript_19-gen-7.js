  const numsArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  return numbers.split(' ').sort((a, b) => numsArr.indexOf(a) - numsArr.indexOf(b)).join(' ');
}

console.log(sortNumbers('three one five'));


// Test cases
console.log(sortNumbers('zero nine five two four seven six one eight three')) //=> "zero one two three four five six seven eight nine"
console.log(sortNumbers('three one five')) //=> "one three five"
console.log(sortNumbers('two two two')) //=> "two two two"
console.log(sortNumbers('')) //=> ""

```

### JavaScript
```javascript
