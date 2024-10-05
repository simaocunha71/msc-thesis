    int max=0;
    int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i]>max)
    max=lst[i];
    string str=to_string(max);
    for (i=0;i<str.length();i++)
    sum+=str[i]-'0';
    return sum;
}


