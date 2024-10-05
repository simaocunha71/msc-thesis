    string upcase="AEIOU";
    string upcase2="aeiou";
    int i;
    int count=0;
    for (i=0;i<s.length();i++)
    {
        if (i%2==0)
        if (find(upcase.begin(),upcase.end(),s[i])!=upcase.end())
        count+=1;
    }
    return count;
}

