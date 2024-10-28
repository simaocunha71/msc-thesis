Here is a Java solution that uses a loop to iterate over the first `k` elements of the array, and checks if the length of the string representation of each element is at most 2. If it is, the element is added to the sum. The method returns the sum.

```java
public int addElements(List<Integer> arr, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        int num = arr.get(i);
        String str = String.valueOf(num);
        if (str.length() <= 2) {
            sum += num;
        }
    }
    return sum;
}
```

You can test this method with the provided example:

```java
public static void main(String[] args) {
    List<Integer> arr = Arrays.asList(111, 21, 3, 4000, 5, 6, 7, 8, 9);
    int k = 4;
    Solution solution = new Solution();
    int result = solution.addElements(arr, k);
    System.out.println(result); // Output: 24
}
```

This will output `24`, which is the sum of `21` and `3`, the elements with at most two digits from the first `k` elements of the array.