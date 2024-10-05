    int i,j;
    int count=0;
    for (i=0;i<str.length();i++)
    for (j=0;j<substring.length();j++)
    if (str[i+j]==substring[j])
    count++;
    return count;
}

