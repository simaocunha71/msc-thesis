    vector<string> result;
    string s;
    int i,n;
    for (i=0;i<lst.size();i++)
    {
        n=0;
        s=lst[i];
        for (int j=0;j<s.length();j++)
        if (s[j]%2!=0)
        n++;
        result.push_back("the number of odd elements "+to_string(n)+"n the str"+to_string(n)+" of the "+to_string(n)+"nput.");
    }
    return result;
}


