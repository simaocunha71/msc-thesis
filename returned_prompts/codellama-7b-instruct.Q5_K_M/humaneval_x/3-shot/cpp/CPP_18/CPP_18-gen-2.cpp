    int count=0;
    int i;
    for (i=0;i<str.length();i++)
    if (str.substr(i,substring.length())==substring)
    count+=1;
    return count;
}


