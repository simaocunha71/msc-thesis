    string strongest_ext;
    float max_strength=-1.0;
    int i;
    for (i=0;i<extensions.size();i++)
    {
        int cap=0,sm=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                cap++;
            else
                sm++;
        }
        float strength=(float)cap-sm;
        if (strength>max_strength){
            max_strength=strength;
            strongest_ext=extensions[i];
        }
    }
    return class_name+"."+strongest_ext;
}
