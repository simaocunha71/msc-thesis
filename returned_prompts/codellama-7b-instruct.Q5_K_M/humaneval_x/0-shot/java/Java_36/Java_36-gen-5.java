        int cnt=0;
        for(int i=1; i<n; i++){
            if(i%11==0 || i%13==0){
                String s = String.valueOf(i);
                for(char ch : s.toCharArray()){
                    if(ch=='7') cnt++;
                }
            }
        }
        return cnt;
    }
}



