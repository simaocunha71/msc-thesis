    int integer;
    int i;
    int len=value.length();
    for (i=0;i<len;i++)
    if (value[i]=='.')
    {
        integer=atoi(value.substr(0,i).c_str());
        int decimals=atoi(value.substr(i+1).c_str());
        if (decimals>=5)
        {
            return integer+1;
        }
        if (decimals<5)
        {
            return integer;
        }
        if (decimals==5)
        {
            return integer+(value[i-1]=='0')?integer+1:integer;
        }
    }
    return atoi(value.c_str());
}


