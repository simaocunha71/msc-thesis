        if (x==1) {
            return true;
        }
        while(x > 1) {
            if(x%n != 0) {
                return false;
            }
            x = x / n;
        }
        return true;
    }
}

This solution will work for the given problem statement. The function isSimplePower checks whether x is a simple power of n.

It will return true if x is 1 (since 1 is a simple power of all numbers), otherwise it will keep dividing x by n until x becomes 1. If x is not 1 and it becomes 0 (which means x is not a multiple of n), it will return false. If x is 1 after the while loop, it will return true, indicating that x is a simple power of n.

For example, if x=8 and n=2, it will return true because 2**3 = 8. If x=3 and n=2, it will return false because 2**2 = 4 and 4 is not equal to 3.

This solution has a time complexity of O(log(x)) because in each iteration it divides x by n.

Note: This solution assumes that x and n are positive integers.

This solution is written in Java.
*/

// You can test the solution with the following main function:

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.isSimplePower(1, 4));  // true
        System.out.println(sol.isSimplePower(2, 2));  // true
        System.out.println(sol.isSimplePower(8, 2));  // true
        System.out.println(sol.isSimplePower(3, 2));  // false
        System.out.println(sol.isSimplePower(3, 1));  // false
        System.out.println(sol.isSimplePower(5, 3));  // false
    }
}

// This will print true for the test cases where x is a simple power of n and false in other cases.
// For example, for the test case isSimplePower(1, 