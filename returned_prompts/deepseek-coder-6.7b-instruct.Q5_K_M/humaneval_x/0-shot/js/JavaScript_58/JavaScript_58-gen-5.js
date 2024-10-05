  const result = [];
  
  //Sort both lists
  l1.sort((a, b) => a - b);
  l2.sort((a, b) => a - b);
  
  //Find common elements
  for(let i = 0; i < l1.length; i++){
    if(l2.includes(l1[i]) && !result.includes(l1[i])){
      result.push(l1[i]);
    }
  }

  //Return sorted unique common elements
  return result;
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8], [3, 2]));

```

