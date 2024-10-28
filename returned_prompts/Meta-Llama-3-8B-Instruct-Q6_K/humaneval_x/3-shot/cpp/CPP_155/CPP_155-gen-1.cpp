    int even_count=0;
    int odd_count=0;
    string str=to_string(abs(num));
    for (int i=0;i<str.length();i++)
    {
        int digit=str[i]-'0';
        if (digit%2==0)
        even_count++;
        else
        odd_count++;
    }
    if (num<0)
    {
        even_count--;
    }
    vector<int> result;
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}  



