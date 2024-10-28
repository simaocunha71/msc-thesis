    int prime,max=-1;
    for(int i=0;i<lst.size();i++){
        prime=lst[i];
        if(prime>1){
            for(int j=2;j*j<=prime;j++){
                if(prime%j==0){
                    prime=0;
                    break;
                }
            }
            if(prime>max)
            max=prime;
        }
    }
    if(max==-1)
    return 0;
    else{
    int sum=0;
    string str_max=to_string(max);
    for(int i=0;i<str_max.length();i++)
    sum+=str_max[i]-'0';
    return sum;
    }
}


