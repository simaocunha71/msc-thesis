    string result;
    int remain;
    while(N>0)
    {
        remain=N%2;
        N=N/2;
        result=to_string(remain)+result;
    }
    return result;
}
