    int count=0;
    for (int i=0;i<str.length()-substring.length()+1;i++)
    if (str.substr(i,substring.length())==substring)
    count+=1;
    return count;
}


