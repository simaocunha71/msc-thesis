    string result="";
    int a=x;
    int i=0;
    while (a>0){
        result+=to_string(a%10);
        a/=10;
        i+=1;
    }
    result=result.substr(shift%i,i-shift%i);
    string rev="";
    int j=result.length()-1;
    while (j>=0)
    rev+=result[j];
    j-=1;
    while (j>=0)
    rev+=result[j];
    return rev;
}


