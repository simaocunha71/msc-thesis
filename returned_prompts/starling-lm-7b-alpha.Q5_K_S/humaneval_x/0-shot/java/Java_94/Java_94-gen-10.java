        int sum = 0;
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < lst.size(); i++) {
            if(isPrime(lst.get(i))) {
                int temp = lst.get(i);
                while(temp > 0) {
                    sum += (temp % 10);
                    temp = temp/10;
                }
                max = Math.max(max, sum);
                sum = 0;
            }
        }
        return max;
    }

    public boolean isPrime(int n) {
        if(n <= 1) {
            return false;
        }
        if(n <= 3) {
            return true;
        }
        if(n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        int i = 5;
        while(i * i <= n) {
            if(n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }
}































































































































































































































