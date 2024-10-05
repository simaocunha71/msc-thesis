    int count=0;
    for(int i=2; i<=a; i++){
        if(a%i==0){
            while(a%i==0){
                a=a/i;
                count++;
            }
        }
    }
    return count==3;
}


