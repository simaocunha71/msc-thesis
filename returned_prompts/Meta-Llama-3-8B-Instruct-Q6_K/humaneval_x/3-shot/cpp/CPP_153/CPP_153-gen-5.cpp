    int i;
    int best_strength=-1;
    string best_extension;
    for (i=0;i<extensions.size();i++)
    {
        int CAP=0;
        int SM=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            if (isupper(extensions[i][j]))
                CAP++;
            else if (islower(extensions[i][j]))
                SM++;
        }
        int strength=CAP-SM;
        if (strength>best_strength)
        {
            best_strength=strength;
            best_extension=extensions[i];
        }
    }
    return class_name+"."+best_extension;
}