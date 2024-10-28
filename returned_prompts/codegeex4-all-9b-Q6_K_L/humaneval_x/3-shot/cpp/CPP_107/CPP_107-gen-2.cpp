    int i;
    int even=0;
    int odd=0;
    for (i=1;i<=n;i++)
    {
        string str=to_string(i);
        if (str==string(str.rbegin(),str.rend()))
        {
            if (i%2==0)
            even+=1;
            else
            odd+=1;
        }
    }
    return {even,odd};
}

