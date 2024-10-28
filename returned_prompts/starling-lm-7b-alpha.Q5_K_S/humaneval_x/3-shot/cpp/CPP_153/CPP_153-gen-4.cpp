    int i,strength_max=-10000;
    string extension_max="";
    for (i=0;i<extensions.size();i++)
    {
        int strength=0;
        int cap=0;
        int sm=0;
        for (int j=0;j<extensions[i].size();j++)
        {
            if ('A'<=extensions[i][j]&&extensions[i][j]<='Z')
            cap+=1;
            if ('a'<=extensions[i][j]&&extensions[i][j]<='z')
            sm+=1;
        }
        strength=cap-sm;
        if (strength>=strength_max)
        {
            strength_max=strength;
            extension_max=extensions[i];
        }
    }
    return class_name+"."+extension_max;
}



