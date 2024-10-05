    int i,max=0,position=0;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>max)
        {
            max=strings[i].length();
            position=i;
        }
    }
    return strings[position];
}

