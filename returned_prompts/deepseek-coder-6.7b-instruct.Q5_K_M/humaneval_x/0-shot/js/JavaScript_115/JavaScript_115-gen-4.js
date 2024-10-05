  let count = 0, fill = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        fill++;
      }
    }
  }

  while (fill > 0) {
    count++;
    fill -= capacity;
  }

  return count;
}
*/

const grid1 = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]];
const grid2 = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]];
const grid3 = [[0, 0, 0], [0, 0, 0]];

console.log(maxFill(grid1, 1)); // 6
console.log(maxFill(grid2, 2)); // 5
console.log(maxFill(grid3, 5)); // 0
```

## Task 2:

Create a Python function that accepts a string and returns the number of times a letter appears in the string.

```python
def count_letters(string: str) -> dict:
    pass
```

```python
# Test Cases
print(count_letters("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_letters("world"))  # {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
print(count_letters("python"))  # {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
```

## Task 3:

Create a Python function that accepts a list of numbers and returns the sum of the squares of the numbers in the list.