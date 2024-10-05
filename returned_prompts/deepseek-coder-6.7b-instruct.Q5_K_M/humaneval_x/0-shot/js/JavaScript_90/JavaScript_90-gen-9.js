  if(lst.length < 2)
    return null;

  let smallest = Infinity;
  let secondSmallest = Infinity;

  for(let i = 0; i < lst.length; i++) {
    if(lst[i] < smallest) {
      secondSmallest = smallest;
      smallest = lst[i];
    } else if(lst[i] > smallest && lst[i] < secondSmallest) {
      secondSmallest = lst[i];
    }
  }

  return secondSmallest === Infinity ? null : secondSmallest;
}

console.log(nextSmallest([1, 2, 3, 4, 5])); // 2
console.log(nextSmallest([5, 1, 4, 3, 2])); // 2
console.log(nextSmallest([])); // null
console.log(nextSmallest([1, 1])); // null
```

This code first checks if the array has less than 2 elements. If so, it returns null. Then, it iterates through each element of the array. If the current element is smaller than the smallest found so far, it updates the smallest and second smallest variables. If the current element is larger than the smallest but smaller than the second smallest, it updates the second smallest. If no second smallest is found, the function returns null. Otherwise, it returns the second smallest.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```