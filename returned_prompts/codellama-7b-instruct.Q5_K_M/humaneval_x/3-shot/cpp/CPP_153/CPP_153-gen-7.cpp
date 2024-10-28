    int i,j;
    float strength_current,strength_max;
    string extension_strongest;
    for (i=0;i<extensions.size();i++)
    {
        strength_current=0;
        strength_max=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
            strength_current+=1;
            else
            strength_current-=1;
        }
        if (strength_current>strength_max)
        {
            strength_max=strength_current;
            extension_strongest=extensions[i];
        }
    }
    return class_name+"."+extension_strongest;
}


