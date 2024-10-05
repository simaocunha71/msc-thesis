    int i,j;
    int res=0;
    int temp=0;
    for (i=0;i<num.length();i++)
    {
        temp=hex_key(num.substr(i,1));
        if (hex_prime(temp)==1)
        res++;
    }
    return res;
}


