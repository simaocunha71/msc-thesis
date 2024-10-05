        if(N == 1){
            return "1";
        }
        else{
            int n = N;
            int sum = 0;
            while(n > 0){
                int d = n % 2;
                sum += d;
                n /= 2;
            }
            return String.valueOf(sum);
        }
    }
}
