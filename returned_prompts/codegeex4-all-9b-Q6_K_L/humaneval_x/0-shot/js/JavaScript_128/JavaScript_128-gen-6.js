```
const prodSigns = (arr) => {
  if(arr.length == 0) return null;
  let prod = 1;
  let sum = 0;
  for(let i = 0; i < arr.length; i++) {
    if(arr[i] == 0) return 0;
    if(arr[i] < 0) prod *= -1;
    sum += Math.abs(arr[i]);
  }
  return sum * prod;
}
```