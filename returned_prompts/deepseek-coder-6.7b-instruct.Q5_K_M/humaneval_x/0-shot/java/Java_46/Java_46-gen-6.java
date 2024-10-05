        if(n<4){
            if(n<0){
                return 0;
            }
            return n;
        }
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 2;
        fib[3] = 0;

        for(int i=4; i<=n; i++){
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
        }

        return fib[n];
    }

public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.fib4(5));
        System.out.println(s.fib4(6));
        System.out.println(s.fib4(7));
    }
}

Explanation:
The function fib4(n) uses a simple iteration method to solve the problem. It first checks if the input number n is smaller than 4, if so, it returns the number itself or 0 (if n is negative). If n is larger than or equal to 4, it creates an array of size n+1 to store the calculated values of the Fib4 sequence. The four base cases (fib4(0), fib4(1), fib4(2), fib4(3)) are initialized in the array. Then it calculates the rest of the sequence by summing up the previous four numbers in the sequence. Finally, it returns the nth number of the Fib4 sequence.
The main function is used to test the function. It prints the results of calling fib4(5), fib4(6), and fib4(7).
*/





























































































