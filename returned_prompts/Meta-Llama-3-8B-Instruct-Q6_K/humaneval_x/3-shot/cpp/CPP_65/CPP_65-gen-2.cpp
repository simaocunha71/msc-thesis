    string s=to_string(x);
    int len=s.length();
    shift%=len;
    if(shift==0)
        return s;
    if(shift>=len)
        return s.substr(len-shift)+s.substr(0,len-shift);
    return s.substr(len-shift)+s.substr(0,len-shift);
}