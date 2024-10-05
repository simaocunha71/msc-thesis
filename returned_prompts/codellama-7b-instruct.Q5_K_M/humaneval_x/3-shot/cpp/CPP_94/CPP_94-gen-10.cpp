    int max=0,sum=0;
    for (int i=0;i<lst.size();i++)
    if (lst[i]>max)
    max=lst[i];
    string str=to_string(max);
    for (int i=0;i<str.length();i++)
    sum+=str[i]-'0';
    return sum;
}




