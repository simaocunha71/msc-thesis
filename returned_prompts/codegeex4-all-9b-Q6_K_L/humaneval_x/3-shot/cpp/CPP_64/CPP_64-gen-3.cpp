    string vowels="aeiouAEIOU";
    int count=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (find(vowels.begin(),vowels.end(),s[i])!=vowels.end())
        count+=1;
    }
    if (s[s.length()-1]=='y' || s[s.length()-1]=='Y')
        count+=1;
    return count;
}

