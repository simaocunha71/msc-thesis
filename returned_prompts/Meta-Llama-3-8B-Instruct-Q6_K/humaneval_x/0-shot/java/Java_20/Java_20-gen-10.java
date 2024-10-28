    public List<Double> findClosestElements(List<Double> numbers) {
        Collections.sort(numbers);
        double minDiff = Double.MAX_VALUE;
        double closest1 = 0, closest2 = 0;
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = numbers.get(i + 1) - numbers.get(i);
            if (diff < minDiff) {
                minDiff = diff;
                closest1 = numbers.get(i);
                closest2 = numbers.get(i + 1);
            }
        }
        List<Double> result = new ArrayList<>();
        result.add(closest1);
        result.add(closest2);
        return result;
    }  // This solution sorts the list of numbers and then iterates through it to find the closest pair of numbers.

    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.2))
    [2.0, 2.2]

    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.0))
    [2.0, 2.0]

This solution has a time complexity of O(n log n) due to the sorting operation. It has a space complexity of O(1) as it uses a constant amount of space to store the result.  // This code was written in Java.  // This is a solution for the problem of finding the closest pair of elements in a list of numbers.  // The problem can be solved by sorting the list and then iterating through it to find the closest pair of numbers.  // The solution is not efficient for large lists of numbers because it uses a sorting algorithm which has a time complexity of O(n log n).  // A more efficient solution would be to use a data structure that allows for efficient searching and insertion, such as a balanced binary search tree or a hash table.  // The solution can be improved by using a more efficient sorting algorithm or by using a different data structure.  // The code can be modified to handle edge cases, such as a list of one or two elements, or a list with duplicate elements.  // The code can be tested using the provided test cases.  // The code is written in Java and uses the Java Collections Framework to sort the list of numbers. 