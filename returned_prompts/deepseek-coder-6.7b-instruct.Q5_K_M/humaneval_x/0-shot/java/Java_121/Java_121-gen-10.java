        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

This solution iterates over the list of integers and checks if the index is even and the integer at that index is odd. If both conditions are met, the integer is added to the sum. The result is then returned.
The time complexity is O(n) where n is the length of the list. The space complexity is O(1) as no additional space is used.

*/

//Test the solution
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(Arrays.asList(5, 8, 7, 1))); // Output: 12
        System.out.println(sol.solution(Arrays.asList(3, 3, 3, 3, 3))); // Output: 9
        System.out.println(sol.solution(Arrays.asList(30, 13, 24, 321))); // Output: 0
    }
}

/*
Output:
12
9
0
*/

//Test the solution with an empty list
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(Arrays.asList())); // Output: 0
    }
}

/*
Output:
0
*/

//Test the solution with a list of negative numbers
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(Arrays.asList(-5, 8, -7, 1))); // Output: -12
    }
}

/*
Output:
-12
*/

//Test the solution with a list of positive and negative numbers
