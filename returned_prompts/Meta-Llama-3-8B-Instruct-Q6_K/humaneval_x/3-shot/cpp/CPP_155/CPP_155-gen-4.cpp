    vector<int> count;
    count.resize(2);
    int i;
    string str;
    str=to_string(abs(num));
    for (i=0;i<str.length();i++)
    {
        if (str[i]%2==0)
        count[0]++;
        else
        count[1]++;
    }
    return count;
}

