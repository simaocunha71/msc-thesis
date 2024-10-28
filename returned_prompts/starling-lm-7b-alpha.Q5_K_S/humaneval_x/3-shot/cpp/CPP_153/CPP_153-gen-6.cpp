    string name_with_strongest;
    int i,j;
    int cap,sm;
    int strength;
    char chr;
    for (i=0;i<extensions.size();i++)
    {
        name_with_strongest="";
        cap=0;
        sm=0;
        chr=extensions[i][0];
        strength=-cap+sm;
        if (chr>='A' && chr<='Z')
        cap+=1;
        if (chr>='a' && chr<='z')
        sm+=1;
        for (j=1;j<extensions[i].length();j++)
        {
            chr=extensions[i][j];
            if (chr>='A' && chr<='Z')
            cap+=1;
            if (chr>='a' && chr<='z')
            sm+=1;
        }
        strength=-cap+sm;
        if (i==0 || strength>=name_with_strongest.strength)
        {
            name_with_strongest=class_name+"."+extensions[i];
        }
    }
    return name_with_strongest;
}


