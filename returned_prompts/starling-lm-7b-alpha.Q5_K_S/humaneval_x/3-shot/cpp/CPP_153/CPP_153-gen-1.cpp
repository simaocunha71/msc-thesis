    int i;
    int cap,sm;
    float strength;
    string strongest_ext;
    for (i=0;i<extensions.size();i++)
    {
        cap=0;
        sm=0;
        strength=float(cap-sm);
        for (char ch:extensions[i])
        {
            if (ch>='A' && ch<='Z')
                cap+=1;
            if (ch>='a' && ch<='z')
                sm+=1;
        }
        if (strength>strength || strength==strength && extensions[i]<strongest_ext)
        {
            strength=strength;
            strongest_ext=extensions[i];
        }
    }
    return class_name+". "+strongest_ext;
}



