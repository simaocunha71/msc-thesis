    int vowels=0;
    sort(s.begin(), s.end());
    for (int i=0;i<s.length();i++)
    if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
    vowels+=1;
    if (s[s.length()-1]=='y')
    vowels+=1;
    return vowels;
}



