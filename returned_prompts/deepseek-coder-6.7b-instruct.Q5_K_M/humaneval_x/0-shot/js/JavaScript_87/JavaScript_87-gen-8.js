  let result = [];
  for(let i = 0; i < lst.length; i++)
    for(let j = 0; j < lst[i].length; j++)
      if(lst[i][j] === x)
        result.push([i, j]);

  result.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

  return result;
};

console.log(getRow([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1));
console.log(getRow([], 1));
console.log(getRow([[], [1], [1, 2, 3]], 3));
/*
Output:
[ [ 0, 0 ], [ 1, 4 ], [ 1, 0 ], [ 2, 5 ], [ 2, 0 ] ]
[]
[ [ 2, 2 ] ]
*/
```

This is a Python solution for the problem:
```python
def getRow(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))

    result.sort(key=lambda x: (x[0], -x[1]))
    return result

print(getRow([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))
print(getRow([], 1))
print(getRow([[], [1], [1, 2, 3]], 3))

# Output:
# [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
# []
# [(2, 2)]
```

The problem can be solved by iterating through the 