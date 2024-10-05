    int i,count=0;
    for (i=0;i<str.length();i++)
    {
        if (str.substr(i,substring.length())==substring)
        count+=1;
    }
    return count;
}



