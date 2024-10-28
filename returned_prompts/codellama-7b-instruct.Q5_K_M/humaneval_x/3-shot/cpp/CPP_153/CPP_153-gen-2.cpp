    int i,j;
    int max_strength=0;
    int strength=0;
    string strongest_extension;
    for (i=0;i<extensions.size();i++)
    {
        strength=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
            strength-=1;
            if (islower(extensions[i][j]))
            strength+=1;
        }
        if (strength>max_strength)
        {
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+"."+strongest_extension;
}




