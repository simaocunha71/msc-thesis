        int i = 0;
        while (i*i*i <= Math.abs(a)) {
            if (i*i*i == Math.abs(a))
                return true;
            i++;
        }
        return false;
    }
}

Explanation:
The function works by iterating over the integers starting from 0. For each integer, it checks if the cube of that integer is equal to the input value 'a'. If it is, the function returns true. If the cube of the integer exceeds 'a' without equaling 'a', the function returns false.
The Math.abs function is used to handle negative values of 'a' by converting them to their positive counterpart before checking if the cube of a number is equal to 'a'.

The time complexity of this solution is O(n), where n is the value of 'a'. This is because in the worst-case scenario, the function has to iterate up to the square root of 'a' times to check if the cube of any integer is equal to 'a'.

In terms of space complexity, the solution is O(1) as it uses a constant amount of space to store the integer 'i' and does not use any additional data structures that scale with the input size.
 */

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.iscube(1)); // true
        System.out.println(solution.iscube(2)); // false
        System.out.println(solution.iscube(-1)); // true
        System.out.println(solution.iscube(64)); // true
        System.out.println(solution.iscube(0)); // true
        System.out.println(solution.iscube(180)); // false
    }
}

/*
Output:
true
false
true
true
true
false
 */

/*
This solution works by iterating over the integers starting from 0. For each integer, it checks if the cube of that integer is equal to the input value 'a'. If it is, the function returns true. If the cube of the integer exceeds 'a' without equ