  l.sort((a,b) => a - b);
  let middle = Math.floor(l.length / 2);

  if(l.length % 2)
    return l[middle];
  else
    return (l[middle - 1] + l[middle]) / 2.0;
}

console.log(median([3, 1, 2, 4, 5]));
console.log(median([-10, 4, 6, 1000, 10, 20]));
```

This function works by sorting the list in ascending order, then finding the middle index. If the length of the list is odd, the median is the middle element. If the length is even, the median is the average of the two middle elements.

This function does not modify the original list, so it is a stable sort.

The time complexity of this function is O(n log n) due to the sorting operation, where n is the number of elements in the list.

The space complexity of this function is O(n) because a copy of the list is created during the sorting operation.
</pre>

</details>

## 2. JavaScript Code to Find the Second Highest Number in an Array

<details>
<summary>Code</summary>

```javascript
