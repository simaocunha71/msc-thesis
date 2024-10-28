    string vowels="aeiou";
    int count=0;
    for (int i=0;i<s.length();i++)
    if (vowels.find(s[i])!=string::npos)
    count+=1;
    return count;
}

