        List<Integer> result = new ArrayList<>(nums);
        Collections.sort(result, new Comparator<Integer>() {
            @Override
            public int compare(Integer i, Integer j) {
                int sum1 = sumOfDigits(i);
                int sum2 = sumOfDigits(j);
                if (sum1 != sum2)
                    return sum1 - sum2;
                return nums.indexOf(i) - nums.indexOf(j);
            }
        });
        return result;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

This solution takes advantage of the built-in sorting function in Java Collections, and uses a custom comparator to order the numbers. The sum of digits is calculated with the `sumOfDigits` method, and if the sums are equal, the original index of the numbers in the input list is used to break ties.

This solution runs in O(n log n) time, where n is the number of elements in the list, because of the sorting operation. The space complexity is O(n) because we create a new list that is a copy of the input list.

I hope this helps!!

```

```python
