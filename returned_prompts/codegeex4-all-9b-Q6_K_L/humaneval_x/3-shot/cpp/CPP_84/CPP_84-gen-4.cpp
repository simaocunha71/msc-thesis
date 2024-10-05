    string ans="";
    int digit;
    while (N>0)
    {
        digit=N%2;
        if (digit==1)
            ans="1"+ans;
        else
            ans="0"+ans;
        N=N/2;
    }
    return ans;
}

