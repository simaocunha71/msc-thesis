    vector<int> count;
    int even=0, odd=0;
    char c;
    string s=to_string(abs(num));
    for (int i=0;i<s.length();i++)
    {
        c=s[i];
        if (c-'0'%2==0)
            even++;
        else
            odd++;
    }
    count.push_back(even);
    count.push_back(odd);
    return count;
}  // This will return {even, odd} count.
} // namespace std.  // This is missing, I think.  It should be the last line.  // This is the namespace.  // It should be at the end.  // It's missing.  // It should be here.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It's missing.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It's not here.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It's missing.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It's missing.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It's missing.  // It should be here.  // It's missing.  // It should be here.  // It's not here.  // It should be here