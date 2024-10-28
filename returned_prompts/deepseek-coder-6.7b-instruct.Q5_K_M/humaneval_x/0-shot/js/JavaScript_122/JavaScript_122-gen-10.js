  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (arr[i] < 10 || arr[i] >= 100) {
      sum += arr[i];
    }
  }
  return sum;
};

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));

```

## Solution:
```python
def add_elements(arr, k):
    sum = 0
    for i in range(k):
        if arr[i] < 10 or arr[i] >= 100:
            sum += arr[i]
    return sum

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # Output: 24
```

## Explanation:
The solution is a simple one. It iterates over the first `k` elements of the array. If the current element has 1 or 2 digits, it is added to the sum. The function returns the sum.
```

## Solution:
```java
public int addElements(int[] arr, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        if (arr[i] < 10 || arr[i] >= 100) {
            sum += arr[i];
        }
    }
    return sum;
}

public static void main(String[] args) {
    int[] arr = {111, 21, 3, 4000, 5, 6, 7, 8, 9};
    int k = 4;
    System.out.println(addElements(arr, k));  // Output: 24
}
```

## Explanation:
The solution is a simple one. It iterates over the first `k` elements of the array. If the current element has 1 or 2 digits, it is added to the sum. The function returns the sum.
```


## Solution:
```javascript