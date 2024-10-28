  if(arr.length === 0){
    return null;
  }
  let sum = 0;
  let prod = 1;
  for(let i=0; i<arr.length; i++){
    if(arr[i] < 0){
      prod *= -1;
    } else if(arr[i] > 0){
      prod *= 1;
    } else {
      return 0;
    }
    sum += Math.abs(arr[i]);
  }
  return prod * sum;
}

console.log(prodSigns([1, 2, 2, -4])); // -9
console.log(prodSigns([0, 1])); // 0
console.log(prodSigns([])); // null
```

## 8. Find the middle element

