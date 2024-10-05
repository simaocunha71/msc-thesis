    string str_x,str_shift;
    int i;
    str_x="";
    for (i=0;i<x;i++)
    {
        str_x+=x%10+'0';
        x/=10;
    }

    if (shift>str_x.length())
    {
        for (i=str_x.length()-1;i>=0;i--)
        {
            str_shift+=str_x[i];
        }
        return str_shift;
    }

    str_shift="";
    for (i=0;i<shift;i++)
    {
        str_shift+=str_x[str_x.length()-i-1];
    }
    for (i=shift;i<str_x.length();i++)
    {
        str_shift+=str_x[i];
    }
    return str_shift;
}



