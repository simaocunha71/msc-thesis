    int i;
    string strongest_ext;
    int strongest_strength=-10000;
    for (i=0;i<extensions.size();i++)
    {
        int cap=0;
        int sm=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                cap++;
            if (islower(extensions[i][j]))
                sm++;
        }
        if (cap-sm>strongest_strength)
        {
            strongest_strength=cap-sm;
            strongest_ext=extensions[i];
        }
    }
    return class_name+"."+strongest_ext;
}   


