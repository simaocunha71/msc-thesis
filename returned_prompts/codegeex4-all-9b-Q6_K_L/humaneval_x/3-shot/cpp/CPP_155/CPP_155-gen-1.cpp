    string str=to_string(num);
    int i;
    int even=0;
    int odd=0;
    for(i=0;i<str.length();i++)
    {
        if (str[i]%2==0)
        even+=1;
        if (str[i]%2!=0)
        odd+=1;
    }
    vector<int> vec={even,odd};
    return vec;
}

