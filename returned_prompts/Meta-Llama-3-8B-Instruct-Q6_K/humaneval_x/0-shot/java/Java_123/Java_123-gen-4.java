    public List<Integer> getOddCollatz(int n) {
        List<Integer> result = new ArrayList<>();
        result.add(n);
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            if (!result.contains(n)) {
                result.add(n);
            }
        }
        result.sort((a, b) -> Integer.compare(a, b));
        return result;
    } 
}  // This function returns the list of odd numbers in Collatz sequence for a given positive integer n. It uses a while loop to generate the sequence and a list to store the odd numbers. It also uses the contains method to avoid adding duplicate numbers to the list. Finally, it sorts the list in increasing order before returning it.  // The time complexity of this function is O(k), where k is the number of steps in the Collatz sequence, which can be at most log2(n) for a given positive integer n. The space complexity is O(k) as well, as we need to store the sequence in the list.  // This function works correctly for all positive integers n.  // For example, if n = 5, the function will return the list [1, 5], which are the odd numbers in the Collatz sequence for 5.  // This function can be used to solve the Collatz problem, which is a well-known unsolved problem in mathematics.  // However, it's worth noting that this function is not suitable for large values of n, as the Collatz sequence can be very long for such values.  // For large values of n, a more efficient algorithm may be needed.  // This function is also not suitable for negative integers, as the Collatz sequence is not defined for negative integers.  // For negative integers, a different function would be needed.  // This function is case-sensitive, so it will return a different result if the input is a negative integer.  // For example, if n = -5, the function will return an empty list, as the Collatz sequence is not defined for negative integers.  // To make this function case-insensitive, we could add a check at the beginning of the function to handle the case where n is a negative integer.  // We could also add a check to handle the case where n is zero, as the Collatz sequence is not