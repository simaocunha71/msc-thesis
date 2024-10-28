  if(strings.length === 0) return null;

  let longest = strings[0];

  for(let i = 1; i < strings.length; i++){
    if(strings[i].length > longest.length){
      longest = strings[i];
    }
  }

  return longest;
}
```

## 5. Reverse a string

