        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return y;
        }
        return x;
    }
}

The code above is a simple function that checks if the given number is prime or not. If it's a prime number, it returns x, else it returns y. The function uses a for loop to check if the number is divisible by any numbers between 2 and square root of the given number. If it is divisible, then it's not a prime number and the function returns y. If it's not divisible by any numbers, then it's a prime number and the function returns x. 

The square root of n is used as the upper limit because a larger factor of n must be a multiple of a smaller factor that has already been checked. 

The time complexity of this function is O(sqrt(n)).
*/

/*
The time complexity of this program is O(sqrt(n)) because in the worst case scenario, it has to check all numbers up to the square root of n to see if they are factors of n. This is a significant improvement over a brute-force method, which would check all numbers up to n.

The space complexity of this program is O(1) because it uses a constant amount of space to store the variables n, x, and y.
*/

// END SOLUTION

// DO NOT MODIFY THE FOLLOWING CODE

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        Solution solution = new Solution();
        System.out.println(solution.xOrY(n, x, y));
    }
}

// END SOLUTION