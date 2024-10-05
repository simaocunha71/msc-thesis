    int max_strength=INT_MIN;
    string strongest_extension="";
    int strength;
    int i;
    for (i=0;i<extensions.size();i++)
    {
        strength=0;
        for (char chr:extensions[i])
        {
            if (chr>='A' && chr<='Z')
                strength+=1;
            else if (chr>='a' && chr<='z')
                strength-=1;
        }
        if (strength>max_strength)
        {
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+'.'+strongest_extension;
}

