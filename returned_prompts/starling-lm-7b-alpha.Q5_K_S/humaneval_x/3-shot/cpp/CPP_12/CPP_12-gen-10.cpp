    int i,max=0;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max)
    max=strings[i].length();

    for (i=0;i<strings.size();i++)
    if (strings[i].length()==max)
    return strings[i];

    return "";
}


