    int i;
    string strongest_extension;
    int strongest_extension_strength = -1000;
    for (i=0;i<extensions.size();i++)
    {
        int cap = 0;
        int sm = 0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                cap++;
            else 
                sm++;
        }
        int extension_strength = cap-sm;
        if (extension_strength > strongest_extension_strength)
        {
            strongest_extension = extensions[i];
            strongest_extension_strength = extension_strength;
        }
    }
    return class_name + "." + strongest_extension;
}  



