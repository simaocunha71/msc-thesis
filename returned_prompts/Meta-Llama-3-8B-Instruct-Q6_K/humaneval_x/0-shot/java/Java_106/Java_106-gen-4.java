        List<Integer> res = new ArrayList<>();
        for(int i=1; i<=n; i++){
            if(i%2==0){
                int fact = 1;
                for(int j=1; j<=i; j++){
                    fact *= j;
                }
                res.add(fact);
            }else{
                int sum = 0;
                for(int j=1; j<=i; j++){
                    sum += j;
                }
                res.add(sum);
            }
        }
        return res;
    }

