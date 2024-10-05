    string ans;
    int remainder;
    while (N>0)
    {
        remainder=N%2;
        ans=to_string(remainder)+ans;
        N=N/2;
    }
    return ans;
}

