    int count=0;
    int i,j;
    for (i=0;i<str.length();i++)
    for (j=i;j<str.length();j++)
    if (str.substr(i,j-i)==substring)
    count+=1;
    return count;
}


