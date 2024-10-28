    int max=-1;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i][0]>='A' && strings[i][0]<='Z' && strings[i][strings[i].length()-1]=='.')
    if (strings[i].length()>max)
    max=strings[i].length();

    return