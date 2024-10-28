    int product=1;
    char chr;
    string str_n=to_string(n);
    int i;
    for (i=0;i<str_n.length();i++)
    {
        chr=str_n[i];
        if ((int)chr%2!=0)
        product*=(int)chr;
    }
    return product;
}


