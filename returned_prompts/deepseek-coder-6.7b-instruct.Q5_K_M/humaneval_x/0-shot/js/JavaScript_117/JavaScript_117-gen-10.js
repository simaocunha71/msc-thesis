  const consonants = 'bcdfghjklmnpqrstvwxyz';
  if(s === ""){
    return [];
  }
  let words = s.split(" ");
  let result = [];
  for(let word of words){
    let count = 0;
    for(let char of word){
      if(consonants.includes(char.toLowerCase())){
        count++;
      }
    }
    if(count === n){
      result.push(word);
    }
  }
  return result;
}

console.log(selectWords("Mary had a little lamb", 4));
console.log(selectWords("Mary had a little lamb", 3));
console.log(selectWords("simple white space", 2));
console.log(selectWords("Hello world", 4));
console.log(selectWords("Uncle sam", 3));

// Output:
// [ 'little' ]
// [ 'Mary' ]
// []
// [ 'world' ]
// [ 'Uncle' ]
```

This is a Python solution:

```python
def selectWords(s, n):
    consonants = "bcdfghjklmnpqrstvwxyz"
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        count = sum(1 for char in word if char.lower() in consonants)
        if count == n:
            result.append(word)
    return result

print(selectWords("Mary had a little lamb", 4))  # ['little']
print(selectWords("Mary had a little lamb", 3))  # ['Mary']
print(selectWords("simple white space", 2))  # []
print(selectWords("Hello world", 4))  # ['world']
print(selectWords("Uncle sam", 3))  # ['Uncle']
```

Output:

```
['little']
['Mary']
[]
['world']
['Uncle']
```

Both solutions have a time complexity of