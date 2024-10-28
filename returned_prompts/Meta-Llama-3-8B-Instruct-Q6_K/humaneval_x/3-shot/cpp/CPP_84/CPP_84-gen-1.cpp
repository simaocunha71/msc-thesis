    int sum=0;
    string binary;
    while(N>0)
    {
        if (N%2!=0)
            sum+=1;
        binary=to_string(N%2)+binary;
        N=N/2;
    }
    ostringstream oss;
    oss<<sum;
    return binary+"."+oss.str();
}

