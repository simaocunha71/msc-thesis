        List<Integer> primes = new ArrayList<>();
        List<Integer> fibs = new ArrayList<>();
        int i = 2;
        while(primes.size() < n || fibs.size() < n){
            if(isPrime(i)){
                primes.add(i);
            }
            if(isFib(i)){
                fibs.add(i);
            }
            i++;
        }
        return primes.get(n - 1);
    }

    private boolean isPrime(int num){
        if(num < 2) return false;
        for(int i = 2; i <= Math.sqrt(num); i++){
            if(num % i == 0) return false;
        }
        return true;
    }

    private boolean isFib(int num){
        if(num < 2) return true;
        int a = 0;
        int b = 1;
        while(b < num){
            int temp = b;
            b = a + b;
            a = temp;
        }
        return b == num;
    }
}

