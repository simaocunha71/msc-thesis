    string bin_string;
    int i,j;
    int n;
    for (i=0;i<5;i++)
    {
        n=N%2;
        N/=2;
        bin_string+=(char)('0'+n);
    }
    return bin_string;
}



