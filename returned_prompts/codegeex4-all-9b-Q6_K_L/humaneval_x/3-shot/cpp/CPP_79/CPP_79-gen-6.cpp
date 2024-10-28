    string bin;
    int bin_len;
    int i;
    int temp=decimal;
    bin_len=0;
    while(temp>0)
    {
        bin_len+=1;
        temp/=2;
    }
    for (i=0;i<bin_len;i++)
    {
        if (decimal%2==1)
        bin+='1';
        else
        bin+='0';
        decimal/=2;
    }

    string binary="db"+bin+"db";
    return binary;
}

