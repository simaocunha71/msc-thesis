    vector<int> result;
    int even=0, odd=0;
    for (int i=1;i<=n;i++)
    {
        string str=to_string(i);
        if (str==reverse(str))
        {
            if (i%2==0)
            even++;
            else
            odd++;
        }
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}
string reverse(string s)
{
    string reversed;
    for(int i=s.length()-1;i>=0;i--)
        reversed+=s[i];
    return reversed;
}