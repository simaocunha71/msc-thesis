```js
const maximum = (arr, k) => {
  const maxHeap = new MaxPriorityQueue({ priority: x => x });
  arr.forEach(num => maxHeap.enqueue(num));
  const result = [];
  for (let i = 0; i < k; i++) {
    result.push(maxHeap.dequeue().element);
  }
  return result.sort((a, b) => a - b);
};
```