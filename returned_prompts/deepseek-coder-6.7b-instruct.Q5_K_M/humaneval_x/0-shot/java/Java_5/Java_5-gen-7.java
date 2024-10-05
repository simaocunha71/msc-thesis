        List<Integer> interspersedList = new ArrayList<>();
        if (!numbers.isEmpty()) {
            interspersedList.add(numbers.get(0));
            for (int i = 1; i < numbers.size(); i++) {
                interspersedList.add(delimiter);
                interspersedList.add(numbers.get(i));
            }
        }
        return interspersedList;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.intersperse(Arrays.asList(1, 2, 3), 4));
    }
}

'''

# Code:

```python
def intersperse(numbers, delimiter):
    interspersed = []
    for i in range(len(numbers)):
        interspersed.append(numbers[i])
        if i != len(numbers) - 1:
            interspersed.append(delimiter)
    return interspersed
```

# Test:

```python
print(intersperse([1, 2, 3], 4))
```

# Output:

```python
[1, 4, 2, 4, 3]
```

# Explanation:

This function takes a list of numbers and a delimiter as input. It creates a new list that has the same elements as the input list, but with the delimiter inserted between each pair of consecutive elements. If the input list is empty, the function returns an empty list.
'''

# Code:

```python
def intersperse(numbers, delimiter):
    interspersed = []
    for i in range(len(numbers)):
        interspersed.append(numbers[i])
        if i != len(numbers) - 1:
            interspersed.append(delimiter)
    return interspersed
```

# Test:

```python
print(inters