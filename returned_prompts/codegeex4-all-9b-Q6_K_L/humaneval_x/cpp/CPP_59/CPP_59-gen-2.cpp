int i;
for(i=2;i<n;i++){
    if(n%i==0){
        int j;
        for(j=2;j<i;j++){
            if(i%j==0){
                break;
            }
        }
        if(j==i){
            return i;
        }
    }
}
return 0;
}