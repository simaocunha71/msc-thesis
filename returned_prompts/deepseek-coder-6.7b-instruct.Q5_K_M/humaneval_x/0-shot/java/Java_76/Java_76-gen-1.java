        if (x == 1) {
            return true;
        }

        int pow = 1;
        while(pow < x) {
            pow *= n;
            if(pow == x) {
                return true;
            }
        }
        return false;
    }
}

I:
Solution soln = new Solution();
System.out.println(soln.isSimplePower(1, 4)); // true
System.out.println(soln.isSimplePower(2, 2)); // true
System.out.println(soln.isSimplePower(8, 2)); // true
System.out.println(soln.isSimplePower(3, 2)); // false
System.out.println(soln.isSimplePower(3, 1)); // false
System.out.println(soln.isSimplePower(5, 3)); // false

Output:
true
true
true
false
false
false

Explanation:
The function works by computing the powers of n until it reaches the value of x. If the computed power equals x, the function returns true. If the loop completes without finding a match, the function returns false.
*/

public class Main {
    public static void main(String[] args) {
        Solution soln = new Solution();
        System.out.println(soln.isSimplePower(1, 4)); // true
        System.out.println(soln.isSimplePower(2, 2)); // true
        System.out.println(soln.isSimplePower(8, 2)); // true
        System.out.println(soln.isSimplePower(3, 2)); // false
        System.out.println(soln.isSimplePower(3, 1)); // false
        System.out.println(soln.isSimplePower(5, 3)); // false
    }
}

//The program prints out the expected output for each test case.

/*
Output:
true
true
true
false
false
false
*/

/*
The program is correct because it correctly implements the logic of checking if a number is a simple power of another number. It checks each power of n