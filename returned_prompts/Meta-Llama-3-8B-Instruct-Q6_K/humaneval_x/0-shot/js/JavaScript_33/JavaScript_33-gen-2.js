```
const sortThird = (l) => {
  return l.map((v, i) => i % 3 === 0 ? [...l.slice(i)].sort().slice(1) : v)
}
```


This function works by using the `map` method to create a new list `l'`. For each element `v` in `l`, it checks if the index `i` is divisible by 3 using the modulus operator `%`. If it is, it creates a new list by slicing `l` from `i` to the end, sorts it, and then takes a slice of the sorted list from the second element (index 1) to the end. This effectively sorts the values at the indices divisible by 3. If the index is not divisible by 3, it just takes the original value `v`. The resulting list `l'` is then returned.