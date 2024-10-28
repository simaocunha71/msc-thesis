    int[] fib4Array = new int[n + 1];
    fib4Array[0] = 0;
    fib4Array[1] = 0;
    fib4Array[2] = 2;
    fib4Array[3] = 0;

    for (int i = 4; i <= n; i++) {
        fib4Array[i] = fib4Array[i - 1] + fib4Array[i - 2] + fib4Array[i - 3] + fib4Array[i - 4];
    }
    return fib4Array[n];
}