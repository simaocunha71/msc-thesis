  const result = [...l]
  const evenIndices = l.filter((_, index) => index % 2 === 0)
  evenIndices.sort((a, b) => a - b)

  for (let i = 0; i < l.length; i += 2) {
    result[i] = evenIndices[i / 2]
  }

  return result
}

sortEven([5, 6, 3, 4])

// Output: [3, 6, 5, 4]
```



---
## Question 4

```javascript
