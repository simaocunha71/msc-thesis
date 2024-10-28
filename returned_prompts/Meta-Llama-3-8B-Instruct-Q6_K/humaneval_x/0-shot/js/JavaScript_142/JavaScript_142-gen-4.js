```
let sum = 0;

for(let i = 0; i < lst.length; i++) {
  if(i % 3 === 0) { // multiple of 3
    sum += lst[i] ** 2; // square the entry
  } else if(i % 4 === 0 && i % 3 !== 0) { // multiple of 4, not multiple of 3
    sum += lst[i] ** 3; // cube the entry
  } else {
    sum += lst[i]; // no operation, just add the entry
  }
}

return sum;
```

Explanation:
This function uses a for loop to iterate over the list. For each entry, it checks if the index is a multiple of 3 or 4 using the modulus operator (`%`). If the index is a multiple of 3, it squares the entry and adds it to the sum. If the index is a multiple of 4 but not a multiple of 3, it cubes the entry and adds it to the sum. If the index is neither a multiple of 3 nor 4, it simply adds the entry to the sum. The function returns the final sum.