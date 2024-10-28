        int sum = 0;
        for(int i = 0; i < lst.size(); i++){
            if(i % 3 == 0) {
                sum += lst.get(i) * lst.get(i);
            } else if(i % 4 == 0) {
                sum += lst.get(i) * lst.get(i) * lst.get(i);
            } else {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

Test Cases:

sumSquares([1, 2, 3]) --> 6
sumSquares([]) --> 0
sumSquares([-1, -5, 2, -1, -5]) --> -126
sumSquares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) --> 110
sumSquares([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) --> 1471
*/

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.sumSquares(Arrays.asList(1, 2, 3))); // 6
        System.out.println(sol.sumSquares(Arrays.asList())); // 0
        System.out.println(sol.sumSquares(Arrays.asList(-1, -5, 2, -1, -5))); // -126
        System.out.println(sol.sumSquares(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))); // 110
        System.out.println(sol.sumSquares(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 