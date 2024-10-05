  l.sort((a, b) => a - b);
  let middle = Math.floor(l.length / 2);

  if(l.length % 2) {
    return l[middle];
  } else {
    return (l[middle - 1] + l[middle]) / 2.0;
  }
}

console.log(median([3, 1, 2, 4, 5]));
console.log(median([-10, 4, 6, 1000, 10, 20]));



A: Here is the JavaScript code that calculates the median of an array:

```javascript
const median = (arr) => {
    const mid = Math.floor(arr.length / 2),
          nums = [...arr].sort((a, b) => a - b);
    return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};

console.log(median([3, 1, 2, 4, 5])); // 3
console.log(median([-10, 4, 6, 1000, 10, 20])); // 8.0
```

In this code, we first create a copy of the input array (`nums`) and sort it in ascending order. Then we check if the array's length is odd. If it is, the median is the middle element, which we get by accessing the middle index (`mid`). If the array's length is even, the median is the average of the two middle elements.

Note: This code assumes that the input array is non-empty and contains only numbers.


























































































