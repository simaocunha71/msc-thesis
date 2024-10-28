The problem can be solved by iterating over the lists and calculating the total number of characters in each list. Then, return the list with the total number of characters less than the other list. If the lists have the same number of characters, return the first list.

Here is the implementation in JavaScript:

```javascript
const totalMatch = (lst1, lst2) => {
  let total1 = 0;
  let total2 = 0;

  for (let str of lst1) {
    total1 += str.length;
  }

  for (let str of lst2) {
    total2 += str.length;
  }

  if (total1 < total2) {
    return lst1;
  } else if (total2 < total1) {
    return lst2;
  } else {
    return lst1;
  }
};
```

This function works by initializing two variables `total1` and `total2` to zero. Then, it iterates over the two lists using a `for...of` loop, adding the length of each string to the corresponding total variable. Finally, it compares the two totals and returns the list with the smaller total. If the totals are equal, it returns the first list.