  if (!strings.length) return null
  let longest = strings[0]
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longest.length) {
      longest = strings[i]
    }
  }
  return longest
}
console.log(longest([]))
console.log(longest(['a', 'b', 'c']))
console.log(longest(['a', 'bb', 'ccc']))
```

## Day 3: Reversing a String

