```js
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  let smallest = Infinity;
  let secondSmallest = Infinity;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < smallest) {
      secondSmallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < secondSmallest && lst[i] > smallest) {
      secondSmallest = lst[i];
    }
  }
  return secondSmallest === Infinity ? null : secondSmallest;
}
```
