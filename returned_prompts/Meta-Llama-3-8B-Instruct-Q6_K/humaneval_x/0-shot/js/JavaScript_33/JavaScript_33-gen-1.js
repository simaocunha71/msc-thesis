```javascript
const sortThird = (l) => {
  return l.map((x, i) => i % 3 === 0 ? l.slice(i).sort((a, b) => a - b).shift() : x)
}
```


Explanation:
The function takes a list `l` as input and returns a new list `l'`. The function uses the `map` method to iterate over the elements of `l`. For each element, it checks if the index `i` is divisible by 3 using the modulo operator `%`. If the index is divisible by 3, it sorts the slice of the list starting from that index (using `slice(i)` and `sort`) and takes the first element of the sorted slice (using `shift`). If the index is not divisible by 3, it simply returns the original element. The resulting list is returned as the output of the function.