  const numMap = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  };

  return numbers.split(' ').sort((a, b) => numMap[a] - numMap[b]).join(' ');
};

console.log(sortNumbers('three one five'));  // 'one three five'
```

## 2. [Find the Missing Number in an Array](https://www.codewars.com/kata/find-the-missing-number-in-an-array)

```javascript
