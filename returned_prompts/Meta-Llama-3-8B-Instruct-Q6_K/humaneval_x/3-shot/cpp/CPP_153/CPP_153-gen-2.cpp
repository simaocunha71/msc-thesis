    int max_strength=-1;
    string strongest_extension;
    for (int i=0;i<extensions.size();i++)
    {
        int cap=0;
        int sm=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                cap++;
            else if (islower(extensions[i][j]))
                sm++;
        }
        int strength=cap-sm;
        if (strength>max_strength)
        {
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}
