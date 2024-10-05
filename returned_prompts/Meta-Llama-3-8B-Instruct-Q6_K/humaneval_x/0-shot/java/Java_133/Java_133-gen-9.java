    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double d : lst) {
            int ceil = (int) Math.ceil(d);
            sum += Math.pow(ceil, 2);
        }
        return sum;
    }
    
    Explanation:
    This solution iterates over each element in the list, rounds it up to the nearest integer using Math.ceil, squares the result using Math.pow, and adds it to the sum. The final sum is then returned.

    Time Complexity: O(n), where n is the number of elements in the list.
    Space Complexity: O(1), as it only uses a constant amount of space to store the sum. 

    For example, if the input list is [1.4, 4.2, 0], the output will be 29. Here's the step-by-step calculation:
    1. Round 1.4 to the nearest integer: 2
    2. Square 2: 4
    3. Add 4 to the sum: 4
    4. Round 4.2 to the nearest integer: 5
    5. Square 5: 25
    6. Add 25 to the sum: 29
    7. Round 0 to the nearest integer: 0
    8. Square 0: 0
    9. Add 0 to the sum: 29

    The final output is 29.