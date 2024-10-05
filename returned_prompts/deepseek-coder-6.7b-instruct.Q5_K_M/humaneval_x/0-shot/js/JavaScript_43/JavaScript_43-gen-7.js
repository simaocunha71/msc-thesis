  const set = new Set();

  for (let num of l) {
    if (set.has(-num)) {
      return true;
    }
    set.add(num);
  }

  return false;
};


```


## 10.4.3 Python Solution

```python
def pairs_sum_to_zero(l):
    nums = set()

    for num in l:
        if -num in nums:
            return True
        nums.add(num)

    return False

print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

## 10.4.4 Java Solution

```java
import java.util.HashSet;

public class Main {
    public static boolean pairsSumToZero(int[] arr) {
        HashSet<Integer> set = new HashSet<>();

        for (int num : arr) {
            if (set.contains(-num)) {
                return true;
            }
            set.add(num);
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(pairsSumToZero(new int[]{1, 3, 5, 0}));  // False
        System.out.println(pairsSumToZero(new int[]{1, 3, -2, 1}));  // False
        System.out.println(pairsSumToZero(new int[]{1, 2, 3, 7}));  // False
        System.out.println(pairsSumToZero(new int[]{2, 4, -5, 3, 5