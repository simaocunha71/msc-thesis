    int sum=0;
    string binary="";
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    while(sum>0){
        binary=to_string(sum%2)+binary;
        sum/=2;
    }
    return binary;
}


