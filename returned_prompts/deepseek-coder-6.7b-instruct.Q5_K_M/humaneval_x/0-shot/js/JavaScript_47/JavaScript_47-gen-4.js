  l.sort((a, b) => a - b);
  let middle = Math.floor(l.length / 2);

  if (l.length % 2) {
    return l[middle];
  } else {
    return (l[middle - 1] + l[middle]) / 2.0;
  }
}

console.log(median([3, 1, 2, 4, 5]));
console.log(median([-10, 4, 6, 1000, 10, 20]));

```

## 2. The Function that Returns the Median

```js
// 1. Sort the list in ascending order
// 2. Find the index of the middle element
// 3. If the list length is odd, return the middle element.
// 4. If the list length is even, return the average of the two middle elements.

const median = (l) => {
  l.sort((a, b) => a - b);
  let middle = Math.floor(l.length / 2);

  if (l.length % 2) {
    return l[middle];
  } else {
    return (l[middle - 1] + l[middle]) / 2.0;
  }
}

console.log(median([3, 1, 2, 4, 5])); // 3
console.log(median([-10, 4, 6, 1000, 10, 20])); // 8.0
```

This function sorts the list in ascending order, then finds the middle index. If the list length is odd, it returns the middle element. If the list length is even, it returns the average of the two middle elements.

## 3. The Function that Returns the Median

```js
// 1. Sort the list in ascending order
// 2. Find the index of the middle element
// 3. If the list length is odd, return the middle element.
// 4. If the list length is even, return the average of the two middle elements.

const median