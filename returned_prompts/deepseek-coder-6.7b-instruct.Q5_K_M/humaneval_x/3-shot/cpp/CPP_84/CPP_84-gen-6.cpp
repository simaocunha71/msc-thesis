    int sum=0;
    while(N>0){
        sum+=N%2;
        N/=2;
    }
    string result="";
    while(sum>0){
        result=(char)('0'+sum%2)+result;
        sum/=2;
    }
    return result;
}

