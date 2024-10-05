    int i,count=0,j;
    for(i=2;i<=a;i++){
        if(a%i==0){
            for(j=2;j<=i;j++){
                if(i%j==0){
                    break;
                }
            }
            if(i==j){
                count++;
            }
            while(a%i==0){
                a=a/i;
            }
        }
    }
    return count==3;
}

