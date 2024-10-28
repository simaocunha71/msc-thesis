        int cube = (int)Math.round(Math.cbrt(a));
        return a == cube*cube*cube;
    }
}

The function works by calculating the cube root of the input integer and rounding it to the nearest whole number. This whole number is then checked to see if it cubed equals the input integer. If the result is true, the function returns true, otherwise it returns false.

*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.iscube(1)); // true
        System.out.println(sol.iscube(2)); // false
        System.out.println(sol.iscube(-1)); // true
        System.out.println(sol.iscube(64)); // true
        System.out.println(sol.iscube(0)); // true
        System.out.println(sol.iscube(180)); // false
    }
}

// This program will output:
// true
// false
// true
// true
// true
// false
// which is the expected output for the given test cases.

// This means the function iscube() is working as expected.


























































































































































































































