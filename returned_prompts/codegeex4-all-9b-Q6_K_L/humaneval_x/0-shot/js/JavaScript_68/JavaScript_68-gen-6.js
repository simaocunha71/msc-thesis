```
const pluck = (arr) => {
  if(arr.length == 0) return [];
  let smallest = [Infinity, Infinity];
  for(let i = 0; i < arr.length; i++){
    if(arr[i] % 2 == 0 && arr[i] < smallest[0]){
      smallest = [arr[i], i];
    }
  }
  return smallest[0] == Infinity ? [] : smallest;
}
```
