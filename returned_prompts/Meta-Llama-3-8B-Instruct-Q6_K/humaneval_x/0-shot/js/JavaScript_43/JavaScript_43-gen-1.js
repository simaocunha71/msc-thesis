```
  let seen = new Set();
  for (let num of l) {
    if (seen.has(-num)) {
      return true;
    }
    seen.add(num);
  }
  return false;
```  