```js
const nextSmallest = (lst) => {
  if (lst.length < 2) {
    return null;
  }
  let smallest = lst[0];
  let nextSmallest = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < smallest) {
      nextSmallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < nextSmallest && lst[i] !== smallest) {
      nextSmallest = lst[i];
    }
  }
  return nextSmallest === smallest ? null : nextSmallest;
}
```