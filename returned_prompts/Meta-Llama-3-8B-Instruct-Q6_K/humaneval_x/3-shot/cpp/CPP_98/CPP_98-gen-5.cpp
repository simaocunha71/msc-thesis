    int count=0;
    for (int i=1;i<s.length();i=i+2)
    {
        if (isupper(s[i]-'a'+65))
        {
            count++;
        }
    }
    return count;
}
// Note: 'a'-'a'+65 is used to convert lowercase to uppercase


