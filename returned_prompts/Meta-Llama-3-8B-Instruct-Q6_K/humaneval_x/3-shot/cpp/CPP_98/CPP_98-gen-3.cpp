    int count=0;
    for (int i=0;i<s.length();i++)
    if (i%2==0 && (s[i]>='A' && s[i]<='Z'))
    count++;
    return count;
}