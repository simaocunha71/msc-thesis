    int i;
    int even=0,odd=0;
    for (i=1;i<=n;i++)
    {
        string str=to_string(i);
        string reverse_str=str;
        reverse(reverse_str.begin(),reverse_str.end());
        if (str==reverse_str)
        {
            if (i%2==0)
            {
                even+=1;
            }
            else
            {
                odd+=1;
            }
        }
    }
    vector<int> even_odd={even,odd};
    return even_odd;
}

