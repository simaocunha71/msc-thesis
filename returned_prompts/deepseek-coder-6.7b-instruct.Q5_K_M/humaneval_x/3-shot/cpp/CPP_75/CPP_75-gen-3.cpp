    int count = 0;
    for(int i=2; i*i<=a; i++){
        while(a%i==0){
            a /= i;
            count++;
        }
    }
    if(a>1) count++;
    return count==3;
}


