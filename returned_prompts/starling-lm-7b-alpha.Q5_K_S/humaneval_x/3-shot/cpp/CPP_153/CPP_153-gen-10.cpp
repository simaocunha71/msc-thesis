    int i;
    int CAP,SM;
    int max_strength=-100000000;
    string strongest_extension;
    for (i=0;i<extensions.size();i++)
    {
        CAP=0;
        SM=0;
        for (char chr:extensions[i])
        {
            if ('A'<=chr&&chr<='Z')
            CAP+=1;
            if ('a'<=chr&&chr<='z')
            SM+=1;
        }
        int strength=CAP-SM;
        if (strength>max_strength){
        max_strength=strength;
        strongest_extension=extensions[i];
        }
    }
    return class_name+". "+strongest_extension;
}




