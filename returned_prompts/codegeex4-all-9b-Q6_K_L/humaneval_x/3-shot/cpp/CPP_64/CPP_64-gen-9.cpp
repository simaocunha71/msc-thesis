    string vowels="aeiouAEIOU";
    int count=0;
    for (int i=0;i<s.size();i++)
    {
        if (find(vowels.begin(),vowels.end(),s[i])!=vowels.end())
        count+=1;
    }
    if (s[s.size()-1]=='y')
    count+=1;
    return count;
}

