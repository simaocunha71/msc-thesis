    int i;
    int max=-100;
    int max_index;
    for (i=0;i<extensions.size();i++)
    {
        int cap=0;
        int sm=0;
        int j;
        for (j=0;j<extensions[i].length();j++)
        {
            char chr=extensions[i][j];
            if (chr>='a' && chr<='z')
            sm+=1;
            if (chr>='A' && chr<='Z')
            cap+=1;
        }
        int strength=cap-sm;
        if (strength>max)
        {
            max=strength;
            max_index=i;
        }
    }
    return class_name+"."+extensions[max_index];
}

