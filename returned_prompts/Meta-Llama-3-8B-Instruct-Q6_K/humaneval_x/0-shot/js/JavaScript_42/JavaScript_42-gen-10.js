```javascript
const incrList = (l) => l.map(x => x + 1);
```
Explanation:
The function `incrList` takes a list `l` as an argument. It uses the `map` method to create a new list where each element is incremented by 1. The `map` method applies a given function to each element of an array and returns a new array with the results. In this case, the function is `x => x + 1`, which adds 1 to each element of the original list. The resulting list is then returned. This solution uses a functional programming approach, which is concise and easy to read. It also preserves the original list and does not modify it.