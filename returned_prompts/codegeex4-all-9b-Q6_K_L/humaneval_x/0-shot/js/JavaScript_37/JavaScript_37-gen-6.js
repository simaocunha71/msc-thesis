The solution is to split the array into two arrays, one containing the even indices and one containing the odd indices. Then, sort the array of even indices, and merge the two arrays back together by alternating between elements of the even and odd arrays. Here's how you can do it in JavaScript:

```javascript
const sortEven = (l) => {
  let evens = l.filter((item, i) => i % 2 === 0);
  let odds = l.filter((item, i) => i % 2 !== 0);
  evens.sort((a, b) => a - b);
  let result = [];
  for (let i = 0; i < Math.max(evens.length, odds.length); i++) {
    if (i < evens.length) {
      result.push(evens[i]);
    }
    if (i < odds.length) {
      result.push(odds[i]);
    }
  }
  return result;
};
```
This function works by first creating two arrays, `evens` and `odds`, which contain the elements at the even and odd indices of the input array, respectively. It then sorts the `evens` array and creates a new array `result`, which starts by adding the elements of the `evens` array and then the elements of the `odds` array. The function then returns the `result` array.