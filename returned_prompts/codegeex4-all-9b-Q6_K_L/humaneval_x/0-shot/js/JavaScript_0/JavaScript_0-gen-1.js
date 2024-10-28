Here is the JavaScript solution for the problem:

```javascript
const hasCloseElements = (numbers, threshold) => {
  for(let i = 0; i < numbers.length - 1; i++) {
    for(let j = i + 1; j < numbers.length; j++) {
      if(Math.abs(numbers[i] - numbers[j]) < threshold) {
        return true;
      }
    }
  }
  return false;
}
```
This function iterates over every pair of numbers in the list and checks if the absolute difference between them is less than the threshold. If it finds such a pair, it immediately returns `true`. If it doesn't find any such pair after checking all pairs, it returns `false`.