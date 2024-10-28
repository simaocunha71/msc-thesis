    int i;
    int c_max=-1;
    int s_max=-1;
    string result;
    for (i=0;i<extensions.size();i++)
    {
        int c=0;
        int s=0;
        for (char chr:extensions[i])
        {
            if (chr>='A' && chr<='Z')
            {
                c+=1;
            }
            if (chr>='a' && chr<='z')
            {
                s+=1;
            }
        }
        int strength=c-s;
        if (strength>c_max)
        {
            c_max=strength;
            s_max=s;
            result=extensions[i];
        }
        else if (strength==c_max && extensions[i]<result)
        {
            c_max=strength;
            s_max=s;
            result=extensions[i];
        }
    }
    return class_name + "." + result;
}



