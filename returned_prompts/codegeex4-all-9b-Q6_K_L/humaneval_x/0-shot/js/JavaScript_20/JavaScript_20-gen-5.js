```javascript
const findClosestElements = (numbers) => {
  var closest = [numbers[0], numbers[1]];
  var minDiff = Math.abs(numbers[0] - numbers[1]);
  for (var i = 0; i < numbers.length - 1; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      var diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < minDiff) {
        minDiff = diff;
        closest = [numbers[i], numbers[j]];
      }
    }
  }
  return closest;
}
```
