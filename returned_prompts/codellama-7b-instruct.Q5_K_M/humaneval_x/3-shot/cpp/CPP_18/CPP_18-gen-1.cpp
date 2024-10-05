    int count=0;
    int i;
    for (i=0;i<str.length();i++)
    if (substring.length()+i<=str.length())
    if (substring==str.substr(i,substring.length()))
    count+=1;
    return count;
}

