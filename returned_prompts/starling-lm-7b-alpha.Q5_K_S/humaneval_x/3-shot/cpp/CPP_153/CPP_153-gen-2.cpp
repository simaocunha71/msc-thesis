    int i,j,max_index;
    int cap,sm;
    string max_ext;
    float max_strength;
    for (i=0;i<extensions.size();i++)
    {
        cap=0;
        sm=0;
        for (j=0;j<extensions[i].length();j++)
        {
            if (extensions[i][j]>='A'&&extensions[i][j]<='Z')
                cap+=1;
            if (extensions[i][j]>='a'&&extensions[i][j]<='z')
                sm+=1;
        }
        float strength=(float)cap-(float)sm;
        if (i==0||strength>max_strength)
        {
            max_strength=strength;
            max_index=i;
            max_ext=extensions[i];
        }
    }
    return class_name+"."+max_ext;
}


