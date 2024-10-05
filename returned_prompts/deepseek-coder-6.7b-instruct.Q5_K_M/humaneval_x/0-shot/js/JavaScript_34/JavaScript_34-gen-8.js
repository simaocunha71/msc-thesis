  const sorted = l.sort((a, b) => a - b);
  return sorted.filter((v, i, a) => v !== a[i - 1]);
};

console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]));

/*
This code takes an array of numbers and first sorts the array in ascending order.
Then, it uses the filter method to create a new array that consists only of unique elements.
This is done by comparing each element to its previous one. If it's different, it's added to the new array.
*/
```


## 2. Array of objects

```javascript
