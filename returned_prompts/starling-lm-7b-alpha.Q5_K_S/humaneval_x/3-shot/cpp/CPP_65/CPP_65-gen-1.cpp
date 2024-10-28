    int i;
    string result;
    int digits=0;
    int temp_x=x;

    for (i=0;temp_x!=0;i++)
    {
        temp_x/=10;
        digits+=1;
    }

    if (shift>=digits)
    {
        for (i=0;i<digits;i++)
        result+=x%10+'0';
        return result;
    }

    result="";
    for (i=0;i<shift;i++)
    result+=x%10+'0';
    x/=10;
    for (i=0;i<digits-shift;i++)
    result+=x%10+'0';
    return result;
}


