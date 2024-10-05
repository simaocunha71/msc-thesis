    int num;
    char chr;
    int i;
    for (i=0;i<value.length();i++)
    {
        chr=value[i];
        if (chr=='.')
        {
        break;
        }
    }
    num=atoi(value.substr(0,i).c_str());
    if (i==value.length())
    {
        return num;
    }
    int dec=atoi(value.substr(i+1).c_str());
    if (dec>=5)
    {
        return num+1;
    }
    return num;
}





