        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int aOnes = Integer.bitCount(a);
                int bOnes = Integer.bitCount(b);

                if (aOnes != bOnes) {
                    return aOnes - bOnes;
                } else {
                    return a - b;
                }
            }
        });

        return arr;
    }
}

This solution uses Java's built-in Integer.bitCount() function to count the number of ones in the binary representation of each number. It then sorts the array using a Comparator, first comparing the counts of ones, and then comparing the decimal values of the numbers themselves when the ones counts are equal.

The Collections.sort() function is used to sort the array in-place. The comparator is passed as an argument to the sort function, and it returns a negative integer, zero, or positive integer as the first argument is less than, equal to, or greater than the second.

The time complexity of this solution is O(n log n), where n is the size of the input array. This is because the sort function used (Collections.sort) has a time complexity of O(n log n). The bitCount() function runs in constant time for each number, and so does the compare() method of the comparator.

The space complexity of this solution is O(n), as the sort function creates a new array of the same size as the input, and this is the only additional space used.

This solution should work for all non-negative integers in the input array. For negative integers, the binary representation is not defined for the standard two's complement system, and so the solution may not work as expected.

Here is a similar solution in Python:

```python
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```

This Python solution uses the built-in `sorted` function with a custom key function. The key function returns a tuple, where the first element is the count of ones in the binary representation of the number, and the second element is the number itself. The `sorted` function then