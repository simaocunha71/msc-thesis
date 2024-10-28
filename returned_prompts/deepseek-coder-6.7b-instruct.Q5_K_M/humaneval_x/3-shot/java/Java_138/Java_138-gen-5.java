        int count = 0;
        int i = 2;
        while(count < 4 && i <= n){
            if(n % i == 0){
                count++;
                n -= i;
            }
            i += 2;
        }
        return count == 4 && n == 0;
    }
}

