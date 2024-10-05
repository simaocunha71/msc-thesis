    int i,j;
    for (i=0;i<s.length();i++)
    for (j=i+1;j<s.length();j++)
    for (j=i+2;j<s.length();j++)
    if (s[i]==s[j] || s[i]==s[j+1] || s[i+1]==s[j] || s[i+1]==s[j+1] || s[i+2]==s[j] || s[i+2]==s[j+1] || s[i+2]==s[j+2])
    return false;
    return true;
}

