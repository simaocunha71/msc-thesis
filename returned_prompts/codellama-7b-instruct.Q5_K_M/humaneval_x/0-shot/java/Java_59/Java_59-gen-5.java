        while(true){
            for(int i = 2; i <= n / 2; i++){
                if(n % i == 0){
                    n = i;
                    continue A;
                }
            }
            break;
        }
        return n;
    }
}






























