    string binary="";
    int sum=0;
    while (N>0)
    {
        sum+=N%2;
        N=N/2;
    }
    return to_string(sum);
}

