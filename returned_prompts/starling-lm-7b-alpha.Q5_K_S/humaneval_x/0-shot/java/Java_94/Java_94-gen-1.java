
        int max = 0;
        int sum = 0;
        for(int i : lst){
            if(isPrime(i)){
                if(sum < i){
                    sum = i;
                    max = 0;
                }
                max += sumOfDigits(sum);
            }
        }
        return max;
    }

    public int sumOfDigits(int num){
        int sum = 0;
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    public boolean isPrime(int num){
        if(num < 2){
            return false;
        }
        for(int i = 2; i*i <= num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
}

























































































































































































































































































