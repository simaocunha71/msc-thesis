        int a = 1;
        int b = 1;
        int fib = 1;
        int count = 0;
        while(count < n){
            fib = a+b;
            a = b;
            b = fib;
            count++;
        }
        return fib;
    }
}

