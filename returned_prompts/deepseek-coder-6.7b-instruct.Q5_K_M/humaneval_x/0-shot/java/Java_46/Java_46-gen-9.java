        if(n < 2) {
            return 0;
        }
        if(n == 2) {
            return 2;
        }
        if(n == 3) {
            return 0;
        }
        
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 2;
        fib[3] = 0;
        
        for(int i = 4; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
        }
        
        return fib[n];
    }
}

This code uses a dynamic programming approach to solve the problem. It initializes an array of size n+1 to keep track of the Fibonacci sequence up to the nth term. It then fills up the array in a bottom-up fashion, by iterating from 4 to n and calculating the nth term as the sum of the previous four terms. The time complexity of this approach is O(n) and the space complexity is O(n).
*/

public class Main
{
    public static void main(String args[])
    {
        Solution solution = new Solution();
        System.out.println(solution.fib4(5)); // 4
        System.out.println(solution.fib4(6)); // 8
        System.out.println(solution.fib4(7)); // 14
    }
}

/*
Output:
4
8
14
*/

This code works by creating a new Solution object and calling the fib4 method on it, passing the desired value of n as an argument. It then prints the result to the console.
*/



















































































