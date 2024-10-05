    if(x==0)return "0";
    char c;
    string res="";
    while(x){
        c=(x%base)+'0';
        res=c+res;
        x/=base;
    }
    return res;








/*
input:
- integer x
- integer base, base is less than 10
return:
- string, string representation