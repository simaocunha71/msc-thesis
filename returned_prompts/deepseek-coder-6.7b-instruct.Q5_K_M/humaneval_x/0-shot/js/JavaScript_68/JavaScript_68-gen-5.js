  if(arr.length === 0){
    return [];
  }

  let smallestEvenValue = Infinity;
  let smallestEvenIndex = Infinity;

  for(let i = 0; i < arr.length; i++){
    if(arr[i] < smallestEvenValue && arr[i] % 2 === 0){
      smallestEvenValue = arr[i];
      smallestEvenIndex = i;
    }
  }

  if(smallestEvenValue === Infinity){
    return [];
  }

  return [smallestEvenValue, smallestEvenIndex];
};

console.log(pluck([4,2,3])); // [2, 1]
console.log(pluck([1,2,3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]

```

### Python

```python

def pluck(arr):
    smallest_even_value, smallest_even_index = float('inf'), float('inf')

    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even_value:
            smallest_even_value = num
            smallest_even_index = i

    if smallest_even_value == float('inf'):
        return []
    
    return [smallest_even_value, smallest_even_index]


print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]

```

### JavaScript

```javascript
const pluck = (arr) => {
  let smallestEvenValue = Infinity;
  let smallestEvenIndex = Infinity;

  for(let i = 0; i < arr.length; i++){
    if(arr[i] < smallest