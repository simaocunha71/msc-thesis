    int i,j,CAP,SM;
    float strength;
    string strongest_extension="";
    for (i=0;i<extensions.size();i++)
    {
        CAP=SM=0;
        for (j=0;j<extensions[i].length();j++)
        if (extensions[i][j]>='A' && extensions[i][j]<='Z')
        CAP+=1;
        for (j=0;j<extensions[i].length();j++)
        if (extensions[i][j]>='a' && extensions[i][j]<='z')
        SM+=1;
        strength=(CAP-SM)/(CAP+SM);
        if (strength>0 && strongest_extension=="" || strength>strongest_extension)
        strongest_extension=extensions[i];
    }
    return class_name+"."+strongest_extension;
}


