  return Array.from(new Set([...l1].filter(i => l2.includes(i))));
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])); // [1, 5, 653]
console.log(common([5, 3, 2, 8], [3, 2])); // [2, 3]

```


## Question 5

```javascript
