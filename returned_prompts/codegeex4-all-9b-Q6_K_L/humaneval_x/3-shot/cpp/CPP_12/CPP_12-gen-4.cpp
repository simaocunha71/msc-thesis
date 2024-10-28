    int i;
    string current_longest="";
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>current_longest.length())
        current_longest=strings[i];
    }
    return current_longest;
}

