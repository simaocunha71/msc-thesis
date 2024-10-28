    int i,vowel_count=0;
    for (i=0;i<s.length();i++)
    if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or (s[i]=='y' and i==s.length()-1))
    vowel_count++;
    return vowel_count;
}



