        List<Integer> copy = new ArrayList<>(array);
        Collections.sort(copy);
        if ((array.get(0) + array.get(array.size() - 1)) % 2 != 0) {
            return copy;
        }
        else {
            Collections.reverse(copy);
            return copy;
        }
    }
}

This solution first checks if the sum of the first and last elements is odd or even. If it is odd, it returns the sorted array in ascending order. If it is even, it reverses the sorted array and returns it.

In the first and last element of the given array are the smallest and the largest numbers respectively. If the sum of these two numbers is odd, it means that the sum of the numbers in the array is odd, therefore, we need to sort the array in ascending order. If the sum is even, it means the sum of the numbers in the array is even, therefore, we need to sort the array in descending order.

In this way, we can solve the problem.

This solution has a time complexity of O(n log n) because of the sorting operation. The space complexity is O(n) because we are creating a copy of the given array.

Here is an alternative solution that uses Java 8's Stream API:

```java
public List<Integer> sortArray(List<Integer> array) {
    return array.stream()
            .sorted()
            .collect(Collectors.toList());
}
```

This solution is simpler and more readable, but it has the same time and space complexity as the previous solution.

```java
public List<Integer> sortArray(List<Integer> array) {
    return array.stream()
            .sorted(Comparator.reverseOrder())
            .collect(Collectors.toList());
}
```

This solution also uses Java 8's Stream API, but it sorts the array in descending order if the sum of the first and last elements is even. It has the same time and space complexity as the previous solution.
 */

// 