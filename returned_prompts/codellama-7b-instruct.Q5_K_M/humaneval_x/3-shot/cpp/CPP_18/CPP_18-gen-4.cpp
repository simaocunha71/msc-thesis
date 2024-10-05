    int i,j,count=0;
    for (i=0;i<str.length();i++)
    for (j=i;j<str.length();j++)
    if (str.substr(i,substring.length())==substring)
    count+=1;
    return count;
}



