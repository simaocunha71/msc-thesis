  return l.map(x => x+1)
}

console.log(incrList([1, 2, 3])) // [2, 3, 4]
console.log(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])) // [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

**Python**

```python
# Python

def incrList(lst):
  return [x+1 for x in lst]

print(incrList([1, 2, 3])) # [2, 3, 4]
print(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])) # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

**JavaScript**

```javascript
// JavaScript

const incrList = (l) => {
  return l.map(x => x+1)
}

console.log(incrList([1, 2, 3])) // [2, 3, 4]
console.log(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])) // [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

**Ruby**

```ruby
# Ruby

def incrList(l)
  return l.map {|x| x+1}
end

puts incrList([1, 2, 3]) # [2, 3, 4]
puts incrList([5, 3, 5, 2, 3, 3, 9, 0, 123]) # [6, 4, 6, 3, 4, 4, 10, 1, 124]
