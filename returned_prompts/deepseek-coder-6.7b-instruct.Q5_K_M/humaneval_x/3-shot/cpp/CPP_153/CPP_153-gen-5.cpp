    int i;
    int strength, max_strength=-10000000;
    string strongest_extension;
    for(i=0;i<extensions.size();i++)
    {
        strength=0;
        for(char & c : extensions[i])
        {
            if(isupper(c))
                strength++;
            else if(islower(c))
                strength--;
        }
        if(strength>max_strength)
        {
            max_strength=strength;
            strongest_extension=extensions[i];
        }
    }
    return class_name+'.'+strongest_extension;
}


