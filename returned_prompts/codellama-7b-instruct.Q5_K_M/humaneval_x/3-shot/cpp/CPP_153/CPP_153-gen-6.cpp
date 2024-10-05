    int class_length=0,extension_length=0,strength=0,strongest_strength=0;
    int i,j;
    for (i=0;i<class_name.length();i++)
    {
        if (class_name[i]>='A'&&class_name[i]<='Z')
        class_length+=1;
    }
    for (j=0;j<extensions.size();j++)
    {
        for (i=0;i<extensions[j].length();i++)
        {
            if (extensions[j][i]>='A'&&extensions[j][i]<='Z')
            extension_length+=1;
        }
        strength=extension_length-(extensions[j].length()-extension_length)/2;
        if (strength>strongest_strength)
        {
            strongest_strength=strength;
            if (strength==class_length)
            return class_name+"."+extensions[j];
        }
    }
    return class_name+"."+extensions[0];
}


