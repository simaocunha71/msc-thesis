    int i,j;
    float strength;
    string strongest_extension_name;
    for (i=0;i<extensions.size();i++)
    {
        strength=float(count(extensions[i].begin(),extensions[i].end(),'A')-count(extensions[i].begin(),extensions[i].end(),'a'));
        if (strength>0){
            if (strongest_extension_name=="")
            strongest_extension_name=extensions[i];
            else
            if (strength>strongest_extension_name.size())
            strongest_extension_name=extensions[i];
        }
    }
    return class_name+"."+strongest_extension_name;
}





