    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        int a = 0, b = 0, c = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    } // This function calculates the nth element of the fibfib sequence. It uses three variables a, b, c to keep track of the previous three elements in the sequence. It starts from the base case where n is 0 or 1, and then iterates from 3 to n to calculate the next element in the sequence. The time complexity is O(n), and the space complexity is O(1). 

B:
    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        int[] fibfib = new int[n + 1];
        fibfib[1] = 0;
        fibfib[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }
        return fibfib[n];
    } // This function calculates the nth element of the fibfib sequence. It uses an array fibfib of size n+1 to store the elements of the sequence. It starts from the base case where n is 0 or 1, and then iterates from 3 to n to calculate the next element in the sequence. The time complexity is O(n), and the space complexity is O(n). 

C:
    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        int[] fibfib = new int[n + 1];
        fibfib[1] = 0;
        fibfib[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }
        return fibfib[n];
    } // This function calculates the nth element of the fib