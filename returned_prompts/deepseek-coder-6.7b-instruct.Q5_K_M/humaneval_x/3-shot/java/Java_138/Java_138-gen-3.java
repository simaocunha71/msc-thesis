        int count = 0;
        for(int i = 2; i <= n; i += 2){
            if(n - i >= 0){
                n -= i;
                count++;
            }
        }
        return count == 4;
    }
}

