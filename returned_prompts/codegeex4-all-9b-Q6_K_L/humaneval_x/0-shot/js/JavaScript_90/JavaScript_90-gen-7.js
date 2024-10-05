```js
const nextSmallest = (lst) => {
  if (!lst || lst.length < 2) return null;
  let smallest = Infinity, secondSmallest = Infinity;
  for (let num of lst) {
    if (num < smallest) {
      secondSmallest = smallest;
      smallest = num;
    } else if (num < secondSmallest && num > smallest) {
      secondSmallest = num;
    }
  }
  return secondSmallest === Infinity ? null : secondSmallest;
}
```