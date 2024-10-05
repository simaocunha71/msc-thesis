class Solution {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) == 1 + 9 + 0 + 0 = 10
    doubleTheDifference(Arrays.asList(-1, -2, 0)) == 0
    doubleTheDifference(Arrays.asList(9, -2)) == 81
    doubleTheDifference(Arrays.asList(0)) == 0

    If the input list is empty, return 0.
     */
    public int doubleTheDifference(List<Object> lst) {

        int sum = 0;
        for (Object n : lst) {
            if (n instanceof Integer) {
                if (((Integer) n) % 2 == 1) {
                    sum += ((Integer) n) * ((Integer) n);
                }
            }
        }
        return sum;
    }
}