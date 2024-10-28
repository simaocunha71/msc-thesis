    string vowels="aeiou";
    int count=0;
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for (int i=0;i<s.length();i++)
    if (find(vowels.begin(), vowels.end(), s[i])!=vowels.end())
    count+=1;
    return count;
}

