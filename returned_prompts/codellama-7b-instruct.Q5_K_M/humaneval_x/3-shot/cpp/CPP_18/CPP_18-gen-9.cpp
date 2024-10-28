    int count=0;
    int i,j;
    for (i=0;i<str.length()-substring.length()+1;i++)
    for (j=0;j<substring.length();j++)
    if (str[i+j]==substring[j])
    count+=1;
    return count;
}


