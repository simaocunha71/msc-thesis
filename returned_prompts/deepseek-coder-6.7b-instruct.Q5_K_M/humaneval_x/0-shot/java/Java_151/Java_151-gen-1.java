        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer && (Integer) obj % 2 != 0 && (Integer) obj > 0) {
                sum += Math.pow((Integer) obj, 2);
            }
        }
        return sum;
    }
}

Here, we first initialize our sum variable to 0. Then we iterate over each object in the list. If the object is an Integer, is positive and odd, we square it and add it to our sum.

Finally, we return the sum. 

Note: This problem can be solved in a more efficient way by using Java 8 Stream API. The given solution is a simple one and easy to understand.

Possible edge cases:
1. If the list contains negative numbers, they are ignored as per the problem statement.
2. If the list contains non-integer numbers, they are also ignored as per the problem statement.
3. If the list contains zero, it is treated as an even number and is not added to the sum.
4. If the list is empty, the function returns 0 as expected.
5. If the list contains numbers that are both odd and positive, they are squared and added to the sum.
6. If the list contains numbers that are both even and positive, they are ignored.
7. If the list contains numbers that are both odd and negative, they are ignored as per the problem statement.
8. If the list contains numbers that are both even and negative, they are ignored as per the problem statement.
*/

//Testing
class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.doubleTheDifference(Arrays.asList(1, 3, 2, 0))); // prints: 10
        System.out.println(sol.doubleTheDifference(Arrays.asList(-1, -2, 0))); // prints: 0
        System.out.println(sol.doubleTheDifference(Arrays.asList(9, -2))); // prints: 81
        System.out.println(sol.doubleTheDifference(Arrays.asList(0))); // prints: 0