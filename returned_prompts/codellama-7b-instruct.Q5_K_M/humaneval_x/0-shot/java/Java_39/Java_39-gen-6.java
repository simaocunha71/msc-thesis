    public int primeFib(int n) {
        for(int i = 0; i < n; i++){
            if(isPrime(fib(i))){
                return fib(i);
            }
        }
        return 0;
    }

    public boolean isPrime(int number){
        if(number == 1){
            return false;
        }
        for(int i = 2; i < number; i++){
            if(number%i == 0){
                return false;
            }
        }
        return true;
    }
    
    public int fib(int n){
        int a = 0;
        int b = 1;
        for(int i = 0; i < n; i++){
            int temp = a + b;
            a = b;
            b = temp;
        }
        return a;
    }
}


