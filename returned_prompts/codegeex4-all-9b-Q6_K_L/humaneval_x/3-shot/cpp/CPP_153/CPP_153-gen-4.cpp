    int max=-1;
    int max_index=0;
    int i,j;
    for (i=0;i<extensions.size();i++)
    {
        int cap=0;
        int sm=0;
        for (j=0;j<extensions[i].length();j++)
        if (isupper(extensions[i][j]))
            cap+=1;
        if (islower(extensions[i][j]))
            sm+=1;
        if (cap-sm>max)
        {
            max=cap-sm;
            max_index=i;
        }
    }
    return class_name+'.'+extensions[max_index];
}