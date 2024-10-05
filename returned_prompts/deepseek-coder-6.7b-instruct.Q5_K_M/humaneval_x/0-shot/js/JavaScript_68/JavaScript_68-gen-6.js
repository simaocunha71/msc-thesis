  if(arr.length === 0){
    return [];
  }

  let smallestEven = Infinity;
  let smallestEvenIndex = -1;

  for(let i = 0; i < arr.length; i++){
    if(arr[i] < smallestEven && arr[i] % 2 === 0){
      smallestEven = arr[i];
      smallestEvenIndex = i;
    }
  }

  return smallestEvenIndex !== -1 ? [smallestEven, smallestEvenIndex] : [];
}

console.log(pluck([4,2,3])) //[2, 1]
console.log(pluck([1,2,3])) //[2, 1]
console.log(pluck([])) //[]
console.log(pluck([5, 0, 3, 0, 4, 2])) //[0, 1]

/*
  In this problem, we initialize smallestEven to Infinity and smallestEvenIndex to -1.
  We then go through every node in the array and if we find a node with a smaller even value
  or if we find a node with the same even value but smaller index, we update smallestEven
  and smallestEvenIndex. Finally, we return [smallestEven, smallestEvenIndex] if smallestEvenIndex
  is not -1, otherwise we return [].
*/
```

---

## **JavaScript**:

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pluck = function(arr) {
    if(arr.length === 0){
        return [];
    }

    let smallestEven = Infinity;
    let smallestEvenIndex = -1;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] < smallestEven && arr[i] % 2 === 0){
            smallestEven = arr[i];
            smallestEvenIndex = i;
        }
    }

    return smallestEvenIndex !== -1 ? [smallestEven, smallestEvenIndex] : [];
};

console.log(pluck([4,2,3])) //[2