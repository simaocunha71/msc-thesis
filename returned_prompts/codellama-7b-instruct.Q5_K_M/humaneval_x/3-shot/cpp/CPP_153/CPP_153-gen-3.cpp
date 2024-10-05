    int i,j;
    int strength,max_strength=0;
    string max_strength_extension;
    for (i=0;i<extensions.size();i++)
    {
        strength=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (extensions[i][j]>='A'&&extensions[i][j]<='Z')
            strength+=extensions[i][j]-'A'+1;
            if (extensions[i][j]>='a'&&extensions[i][j]<='z')
            strength-=extensions[i][j]-'a';
        }
        if (strength>max_strength)
        {
            max_strength=strength;
            max_strength_extension=extensions[i];
        }
    }
    return class_name+"."+max_strength_extension;
}




