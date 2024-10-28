    int count=0;
    for (int i=0;i<s.length();i++)
    {
        if ((s[i]=='a') || (s[i]=='e') || (s[i]=='i') || (s[i]=='o') || (s[i]=='u') || (i==s.length()-1 && s[i]=='y'))
        {
            count++;
        }
    }
    return count;
}
//or
int vowels_count(string s){
    int count=0;
    for (int i=0;i<s.length();i++)
    {
        if ((s[i]=='a') || (s[i]=='e') || (s[i]=='i') || (s[i]=='o') || (s[i]=='u') || (s[i]=='y'))
        {
            if (i==s.length()-1)
                continue;
            count++;
        }
    }
    return count;
}