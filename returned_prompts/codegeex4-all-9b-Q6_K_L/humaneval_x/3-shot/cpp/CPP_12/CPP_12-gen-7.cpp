    int i,j;
    string longest="";
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>longest.length())
        longest=strings[i];
    return longest;
}

