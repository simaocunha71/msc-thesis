    string s;
    while(x){
        s=s+(char)((x%10)+'0');
        x=x/10;
    }
    int len=s.length();
    shift=shift%len;
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(len-shift,len);
        string s2=s.substr(0,len-shift);
        return s1+s2;
    }
}

string circular_shift(int x,int shift){

B:
    string s;
    while(x){
        s=s+(char)((x%10)+'0');
        x=x/10;
    }
    int len=s.length();
    shift=shift%len;
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(shift,len);
        string s2=s.substr(0,shift);
        return s1+s2;
    }
}

string circular_shift(int x,int shift){

C:
    string s;
    while(x){
        s=s+(char)((x%10)+'0');
        x=x/10;
    }
    int len=s.length();
    shift=shift%len;
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(len-shift,len);
        string s2=s.substr(0,len-shift);
        return s1+s2;
    }
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(shift,len);
        string s2=s.substr(0,shift);
        return s1+s2;
    }
}

string circular_shift(int x,int shift){

D:
    string s;
    while(x){
        s=s+(char)((x%10)+'0');
        x=x/10;
    }
    int len=s.length();
    shift=shift%len;
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(len-shift,len);
        string s2=s.substr(0,len-shift);
        return s1+s2;
    }
    if(shift==0){
        return s;
    }
    else{
        string s1=s.substr(len-shift,len);
        string s2=s.substr(0,len-shift);
        return s1+s2;
    }
}
E:
    string s;
    while(x){
        s=s+(char)((x%10)+'0');
        x=x/10;
    }
    int len=s.length();
    shift=shift%len;
    if(shift