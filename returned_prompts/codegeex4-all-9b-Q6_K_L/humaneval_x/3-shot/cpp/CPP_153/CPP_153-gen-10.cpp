    int i,max=-2;
    int j;
    int cap,sm;
    string strongest_extension;
    for (i=0;i<extensions.size();i++)
    {
        cap=0;
        sm=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
            cap+=1;
            else sm+=1;
        }
        if (cap-sm>max){
            strongest_extension=extensions[i];
            max=cap-sm;
        }
    }
    return class_name+'.'+strongest_extension;
}

