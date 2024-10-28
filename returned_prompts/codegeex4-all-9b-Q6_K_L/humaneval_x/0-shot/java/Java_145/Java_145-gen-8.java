```java
public List<Integer> orderByPoints(List<Integer> nums) {
    if (nums == null || nums.size() == 0) {
        return Collections.emptyList();
    }
    List<Integer> result = new ArrayList<>(nums);
    result.sort((o1, o2) -> {
        int sum1 = sumOfDigits(o1);
        int sum2 = sumOfDigits(o2);
        return Integer.compare(sum1, sum2) == 0 ? Integer.compare(nums.indexOf(o1), nums.indexOf(o2)) : Integer.compare(sum1, sum2);
    });
    return result;
}

private int sumOfDigits(int number) {
    int sum = 0;
    while (number != 0) {
        sum += number % 10;
        number = number / 10;
    }
    return sum;
}
```