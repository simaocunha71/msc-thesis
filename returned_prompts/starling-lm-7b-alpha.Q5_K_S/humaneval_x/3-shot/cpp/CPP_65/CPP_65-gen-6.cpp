    int len=0,digit;
    string str="";
    while (x!=0)
    {
        digit=x%10;
        x=x/10;
        len+=1;
        str+=digit+'0';
    }
    if (shift<len)
    {
        char chr=str[shift];
        str.erase(shift,1);
        str.insert(0,chr);
    }
    else
    {
        char chr=str[shift%len];
        str.erase(shift%len,1);
        str.insert(0,chr);
    }

    return str;
}



