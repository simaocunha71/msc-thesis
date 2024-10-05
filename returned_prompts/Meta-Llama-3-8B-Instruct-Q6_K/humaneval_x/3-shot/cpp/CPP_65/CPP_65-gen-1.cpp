    int digits=0;
    int temp=x;
    while(temp>0)
    {
        temp/=10;
        digits++;
    }
    shift %= digits;
    if(shift==0)
        return to_string(x);
    string num=to_string(x);
    return num.substr(shift)+num.substr(0,shift);
}


