    int cap=0;
    int sm=0;
    string strongest_extension;
    int strongest_strength=0;
    for (int i=0;i<extensions.size();i++)
    {
        cap=0;
        sm=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (extensions[i][j]>='A' && extensions[i][j]<='Z')
            cap+=1;
            if (extensions[i][j]>='a' && extensions[i][j]<='z')
            sm+=1;
        }
        int strength=cap-sm;
        if (strength>strongest_strength)
        {
            strongest_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}


